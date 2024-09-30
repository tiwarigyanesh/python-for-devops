import boto3

s3_client = boto3.client('s3',region_name='eu-north-1')

response = s3_client.create_bucket(

    Bucket='gt-boto3-1',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-north-1'
    }
    
)