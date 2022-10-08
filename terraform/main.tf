module "lambda_function" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = var.lambda_function_config.name
  description   = var.lambda_function_config.description
  handler       = var.lambda_function_config.handler
  runtime       = var.lambda_function_config.runtime

  create_package         = var.lambda_function_config.create_package
  local_existing_package = var.lambda_function_config.local_existing_package

  attach_policy = true
  policy        = "arn:aws:iam::aws:policy/AmazonS3FullAccess"

  tags = var.lambda_function_config.tags
}
