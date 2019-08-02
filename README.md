# snapshotalyzer-84
Demo project , manage aws ec2 instance snapshots

## About

This project is a demo and uses boto3 to manage AWS EC2 instance snapshots.

## Configuring

shotty uses th configuration file created by the AWS cli, eg:
`aws configure --profile shotty`

## Running
`pipenv run python shotty/shotty.py <command> <--project=PROJECT>`

*command* is list, start or stop
*project* is optional