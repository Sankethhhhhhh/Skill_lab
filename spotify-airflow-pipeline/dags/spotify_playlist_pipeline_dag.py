from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

import pandas as pd
import os

from spotify_extractor import fetch_playlist_data
from data_transformer import transform_playlist_data, generate_summary_stats
from mood_classifier import classify_mood
from analytics import run_analytics
from visualization import create_visualizations
from config import Config


# -------------------------------
# TASK FUNCTIONS
# -------------------------------

def extract_task(**context):
    """Fetch playlist data from Spotify."""
    
    Config.validate()

    df = fetch_playlist_data()

    if df.empty:
        raise ValueError("No data fetched from Spotify")

    os.makedirs("/tmp", exist_ok=True)

    raw_path = "/tmp/playlist_raw.csv"
    df.to_csv(raw_path, index=False)

    context["ti"].xcom_push(key="raw_data_path", value=raw_path)


def transform_task(**context):
    """Clean and transform the raw playlist dataset."""

    raw_path = context["ti"].xcom_pull(
        key="raw_data_path",
        task_ids="extract_playlist_data"
    )

    df = pd.read_csv(raw_path)

    transformed_df = transform_playlist_data(df)
    transformed_df = classify_mood(transformed_df)

    transformed_path = "/tmp/playlist_transformed.csv"
    transformed_df.to_csv(transformed_path, index=False)

    context["ti"].xcom_push(key="transformed_path", value=transformed_path)


def analytics_task(**context):
    """Run analytics and generate summary report."""

    transformed_path = context["ti"].xcom_pull(
        key="transformed_path",
        task_ids="transform_playlist_data"
    )

    df = pd.read_csv(transformed_path)

    run_analytics(df)

    summary_text = generate_summary_stats(df)

    os.makedirs("/tmp/reports", exist_ok=True)

    with open("/tmp/reports/summary_report.txt", "w", encoding="utf-8") as f:
        f.write(summary_text)


def visualization_task(**context):
    """Generate charts."""

    transformed_path = context["ti"].xcom_pull(
        key="transformed_path",
        task_ids="transform_playlist_data"
    )

    df = pd.read_csv(transformed_path)

    os.makedirs("/tmp/visuals", exist_ok=True)

    create_visualizations(df)


# -------------------------------
# DAG DEFINITION
# -------------------------------

with DAG(
    dag_id="spotify_playlist_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["spotify", "etl", "data_pipeline"]
) as dag:

    extract = PythonOperator(
        task_id="extract_playlist_data",
        python_callable=extract_task
    )

    transform = PythonOperator(
        task_id="transform_playlist_data",
        python_callable=transform_task
    )

    analytics = PythonOperator(
        task_id="run_analytics",
        python_callable=analytics_task
    )

    visualize = PythonOperator(
        task_id="generate_visualizations",
        python_callable=visualization_task
    )

    extract >> transform >> analytics >> visualize