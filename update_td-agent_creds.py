#!/usr/bin/python3

import json
import boto3
import argparse
import sys

parser = argparse.ArgumentParser(description="Parser")
parser.add_argument("secret_name", type=str)
parser.add_argument("region", type=str)

args=parser.parse_args()

session = boto3.session.Session()
client = session.client(service_name='secretsmanager', region_name=args.region)

secrets = json.loads(client.get_secret_value(SecretId=args.secret_name)["SecretString"])

f = open("/var/lib/td-agent/.bashrc", "a")

for key, value in secrets.items():
    if key == "sqs_url":
        f.write('export td-agent_sqs_queue="' + value + '"')
    if key == "sqs_publish_key":
        f.write('export td-agent_sqs_key="' + value + '"')
    if key == "sqs_publish_secret_key":
        f.write('export td-agent_sqs_secret_key="' + value + '"')