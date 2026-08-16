"""Small boto3 helpers for common S3 file and bucket operations."""

import os
from pathlib import Path

import boto3


def build_s3_client():
    """Create an S3 client using boto3's normal credential chain.

    Set S3_ENDPOINT_URL when working with an S3-compatible service rather than
    the default AWS S3 endpoint.
    """
    endpoint_url = os.getenv("S3_ENDPOINT_URL") or None
    return boto3.client("s3", endpoint_url=endpoint_url)


s3_client = build_s3_client()


def download_file(bucket_name, object_key, local_filename):
    destination = Path(local_filename)
    destination.parent.mkdir(parents=True, exist_ok=True)
    s3_client.download_file(bucket_name, object_key, str(destination))


def download_files(bucket_name, files_to_download, local_path):
    destination = Path(local_path)
    destination.mkdir(parents=True, exist_ok=True)
    for object_key in files_to_download:
        download_file(bucket_name, object_key, destination / Path(object_key).name)


def upload_file(local_filename, bucket_name, object_key):
    s3_client.upload_file(str(local_filename), bucket_name, object_key)


def upload_files(local_files, bucket_name, prefix=""):
    prefix = prefix.strip("/")
    for local_file in local_files:
        local_file = Path(local_file)
        object_key = local_file.name if not prefix else f"{prefix}/{local_file.name}"
        upload_file(local_file, bucket_name, object_key)


def list_buckets():
    return [bucket["Name"] for bucket in s3_client.list_buckets().get("Buckets", [])]


def list_objects(bucket_name, prefix=""):
    paginator = s3_client.get_paginator("list_objects_v2")
    objects = []
    for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):
        objects.extend(item["Key"] for item in page.get("Contents", []))
    return objects


def create_bucket(bucket_name):
    s3_client.create_bucket(Bucket=bucket_name)


def delete_object(bucket_name, object_key):
    s3_client.delete_object(Bucket=bucket_name, Key=object_key)


def delete_bucket(bucket_name):
    """Delete an empty bucket."""
    s3_client.delete_bucket(Bucket=bucket_name)


if __name__ == "__main__":
    print("Available buckets:")
    for bucket in list_buckets():
        print(f"- {bucket}")
