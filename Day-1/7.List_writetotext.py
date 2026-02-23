import boto3
import csv

import boto3

s3 = boto3.resource("s3", region_name="ap-south-1")
my_bucket =s3.Bucket("de-sixth-sem-lab-2026")

text_file_location = r"C:\Projects\skill lab\bucket_objects.txt"

with open(text_file_location, "w") as text_file:
    for obj in my_bucket.objects.all():
        if obj.key.endswith(".txt"):
            print(obj.key)
            text_file.write(obj.key + "\n")

print("Text file created successfully.")