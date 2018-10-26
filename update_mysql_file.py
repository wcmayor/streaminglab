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

f = open("/root/mysql-init.sql", "a")

for key, value in secrets.items():
    if key == "apache_insert_password":
        f.write("create user apache_insert@localhost identified by '" + value + "';\n")
        f.write("grant insert, update on apache_logs.* to apache_inser@localhost;\n")
    if key == "root_password":
        f.write("UPDATE mysql.user SET Password=PASSWORD('" + value + "') WHERE User='root';\n")