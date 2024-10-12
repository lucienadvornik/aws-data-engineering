#### LAMBDA for copy file from source S3 bucket to destination S3 bucket #### 

# Import libraries 
import boto3

# Initialize S3 client
s3_client = boto3.client('S3')

# Def function
def lambda_handler(event, context):
    # Source bucket
    source_bucket = event['Records'][0]['s3']['bucket']['name']
     #F Fle key in source bucket
    source_key = event['Records'][0]['s3']['bucket']['name']

    # Destination bucekt
    destination_bucket = 'target_bucket'

    # Copy object to the destination bucket
    s3_client.copy_object(Bucket = destination_bucket,
                          CopySource={'Bucket', source_bucket, 'Key': source_key},
                          Key = source_key)
    
    # Optional - delete the file from the source bucket after copying
    # s3_client.delete_object(Bucket=source_bucket, Key=source_key)