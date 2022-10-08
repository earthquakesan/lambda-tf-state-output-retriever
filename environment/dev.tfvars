lambda_function_config = {
  name                   = "lambda-tfstate-output-retriever-dev"
  description            = "Lambda function to retrieve tfstate outputs from an S3 bucket"
  handler                = "lambda_handler.handler"
  runtime                = "python3.9"
  source_path            = "../src"
  create_package         = false
  local_existing_package = "../lambda_handler.zip"
  tags = {
    "environment" = "dev"
  }
}
