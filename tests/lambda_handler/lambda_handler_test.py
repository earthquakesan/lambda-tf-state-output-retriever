import os

from lambda_handler.lambda_handler import *

BUCKET = "lambda-tfstate-output-retriever-tfstate"
BUCKET_KEY = os.environ.get("BUCKET_KEY", "dev")

def test_retrieve_terraform_state():
    tfstate = retrieve_terraform_state(BUCKET, BUCKET_KEY)
    assert "lambda_function_url" in tfstate

def test_format_terraform_state_to_json():
    tfstate = retrieve_terraform_state(BUCKET, BUCKET_KEY)
    tfstate_json = format_terraform_state_to_json(tfstate)
    assert "lambda_function_url" in tfstate_json

def test_filter_output_by_key():
    tfstate = retrieve_terraform_state(BUCKET, BUCKET_KEY)
    tfstate_filtered = filter_output_by_key(tfstate, 'lambda_function_url')
    assert 'value' in tfstate_filtered
    assert 'type' in tfstate_filtered
