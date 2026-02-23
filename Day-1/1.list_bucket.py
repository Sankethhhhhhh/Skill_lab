import boto3

s3=boto3.resource(
    "s3" ,
    access_key_id="key",
    access_key="key",
    region_name="ap-south-1",
)
for bucket in s3.buckets.all():
    print(bucket.name)