'''Gets info about the users whose tweets are retrieves'''
import json
import boto3

client = boto3.client("dynamodb")
table_name = 'arduino_twitter_users'

def lambda_handler(event, context):
  if 'user_id' in event:
    return get_user(event['user_id'])
  return get_users()

def get_user(user_id: str) -> dict:
  user_resp = client.query(
    TableName=table_name,
    KeyConditionExpression='id = :id',
    ExpressionAttributeValues={
      ':id': {'S': user_id}
    }
  )
  resp_items = user_resp['Items']
  statusCode = 200 if len(resp_items)==1 else 404 if len(resp_items)==0 else 504
  user =resp_items[0] if len(resp_items)==1 else None
  return {
    'statusCode': statusCode,
    'body': user
  }

def get_users():
  resp = client.scan(TableName='arduino_twitter_users', Limit=10)

  return {
    'statusCode': 200,
    'body': [e['id']['S'] for e in resp['Items']]
  }
