import boto3
import os
import boto3

s3 = boto3.resource("s3", region_name="ap-south-1")
my_bucket = s3.Bucket("de-sixth-sem-lab-2026")

working_dir=f"C:\Projects\skill lab"

for file in my_bucket.objects.filter(Prefix="csv/"):
    if file.key.endswith(".txt"):
        local_file_name= os.path.basename(file.key)

        print(f"Downloading {file.key} to {local_file_name}")
        my_bucket.download_file(file.key, local_file_name)
        print(f"Downloaded {file.key} to {local_file_name}")