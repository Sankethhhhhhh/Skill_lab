import boto3
import os

import boto3

s3 = boto3.resource("s3", region_name="ap-south-1")

my_bucket = s3.Bucket("de-sixth-sem-lab-2026")

local_upload_dir = r"C:\Projects\skill lab"
working_dir=r"C:\Projects\skill lab"
for image in os.listdir(local_upload_dir):
    full_upload_path = os.path.join(local_upload_dir, image)
    print(f"Uploading {full_upload_path} to submissions/{image}")
    my_bucket.upload_file(full_upload_path, f"submissions/{image}")
