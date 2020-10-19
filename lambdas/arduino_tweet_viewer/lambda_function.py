import json
import boto3

client = boto3.client("dynamodb")

def lambda_handler(event, context):
  if 'user_id' in event:
    return get_user(event['user_id'])
  return get_users()

def get_users():
  resp = client.scan(TableName='arduino_twitter_users', Limit=10)

  return {
    'statusCode': 200,
    'body': resp
  }
