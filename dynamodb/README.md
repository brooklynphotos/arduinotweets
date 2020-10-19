# Manage DynamoDB Tables for the Project

## Users
### Create
```bash
aws dynamodb create-table \
    --table-name arduino_twitter_users \
    --attribute-definitions AttributeName=id,AttributeType=S  \
    --key-schema AttributeName=id,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=3,WriteCapacityUnits=2 \
    --profile
```
### Drop
`aws dynamodb delete-table --table-name arduino_twitter_users`

## Tweets
### Create
```bash
aws dynamodb create-table \
    --table-name arduino_tweets \
    --attribute-definitions AttributeName=user_id,AttributeType=S AttributeName=id,AttributeType=S  \
    --key-schema AttributeName=user_id,KeyType=HASH AttributeName=id,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --profile
```
### Drop
`aws dynamodb delete-table --table-name arduino_tweets`