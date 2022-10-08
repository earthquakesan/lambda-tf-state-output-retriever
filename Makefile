.PHONY: test
include .env

TF_RUN=terraform -chdir=terraform

tf-init:
	$(TF_RUN) init -reconfigure \
	-backend-config="bucket=${TFSTATE_BUCKET}" \
	-backend-config="key=${BUCKET_KEY}" \
	-backend-config="region=${AWS_REGION}"

plan: tf-init
	$(TF_RUN) plan \
		-var-file=../environment/${ENV}.tfvars \
		-input=false

apply: assemble-lambda-package tf-init
	$(TF_RUN) apply -auto-approve \
		-var-file=../environment/${ENV}.tfvars \
		-input=false

destroy: tf-init
	$(TF_RUN) destroy -auto-approve \
		-var-file=../environment/${ENV}.tfvars \
		-input=false

test:
	BUCKET_KEY=${BUCKET_KEY} pytest -s

LAMBDA_PACKAGE_OUT=lambda_handler.zip

assemble-lambda-package:
	pip install --target ./package -r requirements.txt
	cd package && zip -r ../${LAMBDA_PACKAGE_OUT} .
	zip -j -g ${LAMBDA_PACKAGE_OUT} src/lambda_handler/lambda_handler.py