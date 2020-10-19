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
  tweets_table = dynamodb.Table('arduino_tweets')
  users_table = dynamodb.Table('arduino_twitter_users')
  affected = []
  user_ids = set()
  with tweets_table.batch_writer(overwrite_by_pkeys=['id', 'user_id']) as batch:
    for t in tweets:
      batch.put_item(
        Item=t
      )
      user_ids.add({'id': t['user_id']})
      affected.append({k: v for k,v in t.items() if k in ['id', 'user_id']})
  with users_table.batch_writer(overwrite_by_pkeys=['user_id']) as batch:
    for u in user_ids:
      batch.put_item(
        Item=u
      )
  return affected