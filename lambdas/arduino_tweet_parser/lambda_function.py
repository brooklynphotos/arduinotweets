'''Takes a message in SQS pushed by twitter_mine and decides what to put into dynamoDB'''

import boto3
import json
from datetime import datetime

def lambda_handler(event, context):
  tweets = retrieve_tweets(event)
  return upsert_db(tweets)

def retrieve_tweets(event: dict) -> list:
    msg_body = event['Records'][0]['body']
    return [{'id': t['id_str'], 'text': t['text'], 'created_at': t['created_at'], 'user_id': t['user_id'], 'timestamp': datetime.utcnow().isoformat()} for t in json.loads(msg_body)['responsePayload']]

def upsert_db(tweets: list) -> list:
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table('arduino_tweets')
  affected = []
  with table.batch_writer(overwrite_by_pkeys=['id', 'user_id']) as batch:
    for t in tweets:
      batch.put_item(
        Item=t
      )
      affected.append({k: v for k,v in t.items() if k in ['id', 'user_id']})
  return affected