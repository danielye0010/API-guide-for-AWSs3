# Python S3 Quickstart with boto3

A compact reference for common Amazon S3 and S3-compatible storage operations in Python using **boto3**.

The helper module covers:

- creating an S3 client
- downloading one or many objects
- uploading one or many files
- listing buckets
- listing objects with pagination
- creating buckets
- deleting objects
- deleting empty buckets

## Install

```bash
pip install -r requirements.txt
```

## Authentication

The code uses boto3's normal AWS credential chain rather than hardcoding credentials in source code. Common options include:

- AWS CLI configuration (`aws configure`)
- environment variables such as `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
- IAM roles when running on AWS infrastructure

Do **not** commit credentials to Git.

## S3-compatible endpoints

For standard AWS S3, no endpoint configuration is needed.

For another S3-compatible service, set:

```bash
export S3_ENDPOINT_URL="https://your-s3-endpoint.example.com"
```

On Windows PowerShell:

```powershell
$env:S3_ENDPOINT_URL="https://your-s3-endpoint.example.com"
```

## Usage

```python
from s3_api_guide import download_file, upload_file, list_objects

# Download
 download_file(
    "my-bucket",
    "datasets/example.csv",
    "downloads/example.csv",
)

# Upload
upload_file(
    "results/output.csv",
    "my-bucket",
    "results/output.csv",
)

# List objects
for key in list_objects("my-bucket", prefix="datasets/"):
    print(key)
```

## Run directly

```bash
python s3_api_guide.py
```

This prints the buckets visible to the active boto3 credentials.

## Notes

`delete_bucket()` deletes an **empty** bucket. Delete contained objects first when required by the storage service.
