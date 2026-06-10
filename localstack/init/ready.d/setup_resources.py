import os
import sys
import traceback

import boto3


def ensure_bucket(s3_client, bucket_name: str) -> None:
    existing = [bucket["Name"] for bucket in s3_client.list_buckets().get("Buckets", [])]
    if bucket_name not in existing:
        region = s3_client.meta.region_name or "us-east-1"
        create_kwargs = {"Bucket": bucket_name}
        if region != "us-east-1":
            create_kwargs["CreateBucketConfiguration"] = {
                "LocationConstraint": region
            }
        s3_client.create_bucket(**create_kwargs)
        print(f"[setup_resources] Created bucket: {bucket_name}", flush=True)
    else:
        print(f"[setup_resources] Bucket already exists: {bucket_name}", flush=True)


def ensure_queue(sqs_client, queue_name: str) -> None:
    sqs_client.create_queue(QueueName=queue_name)
    print(f"[setup_resources] Ensured queue: {queue_name}", flush=True)


def main() -> None:
    region = os.getenv("AWS_DEFAULT_REGION", "eu-west-1")
    endpoint_url = "http://localhost:4566"

    print(
        f"[setup_resources] Starting resource bootstrap against {endpoint_url} in region {region}",
        flush=True,
    )

    session = boto3.session.Session(
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID", "test"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", "test"),
        region_name=region,
    )

    s3_client = session.client("s3", endpoint_url=endpoint_url)
    sqs_client = session.client("sqs", endpoint_url=endpoint_url)

    ensure_bucket(s3_client, "agrofalcon-facturas")
    ensure_bucket(s3_client, "agrofalcon-pedidos")

    ensure_queue(sqs_client, "new-leads")
    ensure_queue(sqs_client, "orders")
    ensure_queue(sqs_client, "invoices")

    print("[setup_resources] Resource bootstrap completed successfully", flush=True)


try:
    main()
except Exception as exc:
    print(f"[setup_resources] Bootstrap failed: {exc}", file=sys.stderr, flush=True)
    traceback.print_exc()
    raise
