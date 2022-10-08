variable "lambda_function_config" {
  type = object({
    name                   = string
    description            = string
    handler                = string
    runtime                = string
    source_path            = string
    create_package         = bool
    local_existing_package = string
    tags                   = map(string)
  })
}