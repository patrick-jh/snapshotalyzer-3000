# snapshotalyzer-3000

Demo project to manage AWS EC2 instant snapshots

## About

This project is a demo, and uses XYZ to manage AWS EC2 instance snapshots.

## Configuring

Shot uses the configuration file created by the AWS CLI e.g.

`aws configure – – profile shot`

## Running

`pipenv run python shot/shot.py <command> <--project=PROJECT`

*command* is instances, volumes, or snapshots
*project* is optional
