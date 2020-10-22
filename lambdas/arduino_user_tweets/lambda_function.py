import json
import boto3

client = boto3.client("dynamodb")
table_name = 'arduino_tweets'

def lambda_handler(event, context):
  return build_rest_response(get_tweets(event['userId'], event.get('pagination')))

def get_tweets(user_id: str, pagination: dict) -> dict:
  params = dict(
    TableName=table_name,
    KeyConditionExpression='user_id = :user_id',
    ExpressionAttributeValues={
      ':user_id': {'S': user_id}
    }
  )
  pagination = pagination or {}
  if 'limit' in pagination:
    params['Limit'] = pagination['limit']
  if 'exclusiveStartKey' in pagination:
    params['ExclusiveStartKey'] = pagination['exclusiveStartKey']

  resp = client.query(**params)
  return {
    "data": [tweet['id']['S'] for tweet in resp['Items']],
    "LastEvaluatedKey": resp.get("LastEvaluatedKey")
  }

def build_rest_response(resp_items: list) -> dict:
  statusCode = 200 if len(resp_items) > 0 else 404
  return {
    'statusCode': statusCode,
    'body': resp_items
  }