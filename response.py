import json
import os
import sys
import boto3
import botocore
import yaml
from utils import bedrock, print_ww
import time

def generate_response(question, modelId="anthropic.claude-v2"):

    boto3_bedrock = bedrock.get_bedrock_client(
        assumed_role=os.environ.get("BEDROCK_ASSUME_ROLE", None),
        region=os.environ.get("AWS_DEFAULT_REGION", None),
        runtime=False
    )

    bedrock_runtime = bedrock.get_bedrock_client(
        assumed_role=os.environ.get("BEDROCK_ASSUME_ROLE", None),
        region=os.environ.get("AWS_DEFAULT_REGION", None)
    )
 
    # Create the prompt following the required format
    prompt_data = f"\n\nHuman: {question}\n\nAssistant:"

    body = json.dumps({"prompt": prompt_data, "max_tokens_to_sample": 4096, "temperature": 0})
    accept = "application/json"
    contentType = "application/json"

    try:
        response = bedrock_runtime.invoke_model(
            body=body, modelId=modelId, accept=accept, contentType=contentType
        )
        response_body = json.loads(response.get("body").read())
        v_response = response_body.get("completion")
        return v_response

    except botocore.exceptions.ClientError as error:
        if error.response['Error']['Code'] == 'AccessDeniedException':
            print(f"\x1b[41m{error.response['Error']['Message']}\
                \nTo troubleshoot this issue please refer to the following resources.\
                \nhttps://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_access_denied.html\
                \nhttps://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html\x1b[0m\n")
        else:
            raise error

# Other functions or classes can be defined here

def my_function():
    print("Hello from my_function!")

# Entry point of the script
if __name__ == "__main__":
    question = input("Enter your question")
    modelId = "anthropic.claude-v2"
    v_response = generate_response(question.strip(), modelId)
    print(v_response)
