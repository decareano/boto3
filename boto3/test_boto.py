import boto3

pinga = boto3.resource('s3')

for i in pinga.buckets.all():
    print(i.name)
