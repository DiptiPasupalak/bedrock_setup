Bedrock Helper Utilities

The readme file demonstrates setting up the boto3 client and showcases basic usage of Bedrock.

Prerequisites:

Before executing the response.py script, ensure the following steps are completed:

1) Make sure you have access to the required model in Bedrock.
2) Set the appropriate role and permissions.
3) AWS Configuration:

Note :- The above pre-requisites setup instructions has been provided in instructions.txt file.

Files Overview:

1) __init__.py: General helper utilities for the workshop notebooks.
2) bedrock.py: Helper utilities for interacting with Amazon Bedrock from Python notebooks.
3) requirements.txt: Lists the required Python packages. Install them using pip install -r requirements.txt.
4) response.py: Execute this Python file to enter your question, and it will provide you with the answer.
5) instructions.txt: Contains instructions to setup the pre-requisites for bedrock.

Usage

1. Configure Prerequisites
Ensure that you have completed the prerequisites, including setting up the appropriate role, permissions, and AWS configuration.

2. Install Required Packages
Install the required Python packages by running the following command:

pip install -r requirements.txt

3. Execute response.py

Run the response.py script to interact with Bedrock. This script allows you to input your question, and it will provide you with the answer.

python response.py

Feel free to explore and utilize these utilities for your Bedrock-related tasks!