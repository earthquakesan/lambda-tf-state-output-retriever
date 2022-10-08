# Lambda TF State Output Retriever App

This is an AWS lambda function app, which returns outputs of TF state from S3 bucket.

## App Requirements

The application requirements were specified as follows:

* Should be a lambda function
* Should retrieve TF state from S3 and return outputs
* Lambda function should be created with terraform
* By default all TF outputs should be returned
* Lambda function should accept an input parameter to return specific TF output

# How to: Setup local env

## Required tools

* [Arkade](https://github.com/alexellis/arkade)

## Setup the repository

```
ark get terraform
python -m pip install awscli
```

## Setup Dev Environment (local)

```
# The following variable also used in terraform
AWS_ACCESS_KEY_ID=foo
AWS_SECRET_ACCESS_KEY=bar
AWS_DEFAULT_REGION=eu-central-1

cat <<EOF > ~/.aws/credentials
[default]
aws_access_key_id = ${AWS_ACCESS_KEY}
aws_secret_access_key = ${AWS_SECRET_ACCESS_KEY}
EOF

cat <<EOF > ~/.aws/config
[default]
region = ${AWS_DEFAULT_REGION}
EOF

APP_NAME=lambda-tfstate-output-retriever
BUCKET_NAME=${APP_NAME}-tfstate

aws s3api create-bucket \
  --bucket ${BUCKET_NAME} \
  --acl authenticated-read \
  --create-bucket-configuration LocationConstraint=eu-central-1

aws s3api put-public-access-block \
  --bucket ${BUCKET_NAME} \
  --public-access-block-configuration BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true

aws s3api put-bucket-versioning --bucket ${BUCKET_NAME} \
  --versioning-configuration Status=Enabled

cat <<EOF > .env
ENV=dev
BUCKET_KEY=dev
TFSTATE_BUCKET=${BUCKET_NAME}
AWS_REGION=${AWS_DEFAULT_REGION}
EOF

pip install -r requirements.txt
pip install -r requirements-dev.txt

cp .env_example .env
```

# Additional features/TODOs

* API testing
