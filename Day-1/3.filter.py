import boto3

import boto3

s3 = boto3.resource("s3", region_name="ap-south-1")
my_bucket = s3.Bucket("de-sixth-sem-lab-2026")

for file in my_bucket.objects.filter(Prefix="csv/"):
    print(my_bucket.name)
    print(file.key)
