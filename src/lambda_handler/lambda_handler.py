import json
from typing import Any, Dict, List

import boto3
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.metrics import Metrics
from aws_lambda_powertools.utilities.typing import LambdaContext

tracer = Tracer()
logger = Logger()
metrics = Metrics()

@tracer.capture_lambda_handler
@metrics.log_metrics
def handler(event: Dict[str, Any], _: LambdaContext) -> str:
    """
    Lambda function to retrieve terraform state from a specific S3 bucket.
    Args:
        event: Lambda event - ignored for now
        context: lambda context
    """
    logger.info(f"Got event {event}")
    logger.info(f"Got context {_}")
    bucket = event.get('bucket', '')
    key = event.get('key', '')
    output_filter_key = event.get('output_filter_key', '')
    tfstate_outputs = retrieve_terraform_state(bucket,key)
    if output_filter_key != '':
        tfstate_outputs = filter_output_by_key(tfstate_outputs, output_filter_key)
    logger.info(f"Got tfstate outputs {tfstate_outputs}")

    return tfstate_outputs

def retrieve_terraform_state(bucket: str, key: str) -> List[str]:
    s3_client = boto3.client('s3')
    tf_state_obj_bytes = s3_client.get_object(Bucket=bucket,Key=key)["Body"].read()
    return json.loads(tf_state_obj_bytes)["outputs"]

def format_terraform_state_to_json(tfstate: Any) -> str:
    return json.dumps(tfstate)

def filter_output_by_key(tfstate: Any, key: str) -> Any:
    return tfstate.get(key, '{}')
