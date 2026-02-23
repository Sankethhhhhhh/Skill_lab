import boto3

import boto3

s3 = boto3.resource("s3", region_name="ap-south-1")
for bucket in s3.buckets.all():
    my_bucket = s3.Bucket(bucket.name)

    for file in my_bucket.objects.all():
        print(f"Bucket:{bucket.name} key:{file:key}")
