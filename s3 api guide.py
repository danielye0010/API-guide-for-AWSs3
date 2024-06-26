# make sure you have the packages installed
import os
import boto3


# Remember to replace placeholder values with actual data when using these functions.
# Set up S3 credentials
S3_ACCESS_KEY_ID = os.getenv('S3_ACCESS_KEY_ID')
S3_SECRET_ACCESS_KEY = os.getenv('S3_SECRET_ACCESS_KEY')

# Setting Up Your S3 Client
s3_client = boto3.client(
    's3',
    endpoint_url='https://campus.s3.wisc.edu',
    aws_access_key_id=S3_ACCESS_KEY_ID,
    aws_secret_access_key=S3_SECRET_ACCESS_KEY
)


# Downloading a Single File from S3
def download_file(bucket_name, object_key, local_filename):
    s3_client.download_file(bucket_name, object_key, local_filename)


# Example: download_file('your-bucket-name', 'your/object/key', 'path/to/your/local/destination')

# Downloading Multiple Files from S3
def download_files(bucket_name, files_to_download, local_path):
    for file_key in files_to_download:
        local_filename = os.path.join(local_path, os.path.basename(file_key))
        s3_client.download_file(bucket_name, file_key, local_filename)


# Example: download_files('your-bucket-name', ['file1.jpg', 'file2.txt'], 'local/path')

# Uploading a Single File to S3
def upload_file(local_filename, bucket_name, object_key):
    s3_client.upload_file(local_filename, bucket_name, object_key)


# Example: upload_file('path/to/your/local/file', 'your-bucket-name', 'your/destination/file_name')

# Uploading Multiple Files to S3
def upload_files(local_files, bucket_name):
    for local_file in local_files:
        file_key = os.path.basename(local_file)
        s3_client.upload_file(local_file, bucket_name, file_key)


# Example: upload_files(['path/to/file1.jpg', 'path/to/file2.txt'], 'your-bucket-name')

# Listing All Buckets
def list_buckets():
    response = s3_client.list_buckets()
    for bucket in response['Buckets']:
        print(bucket['Name'])


# Example: list_buckets()

# Creating a New Bucket
def create_bucket(bucket_name):
    s3_client.create_bucket(Bucket=bucket_name)


# Example: create_bucket('unique-bucket-name')

# Deleting a Bucket
def delete_bucket(bucket_name):
    s3_client.delete_object(Bucket=bucket_name, Key=object_key)

# Example: delete_object('your-bucket-name', 'object-key')

