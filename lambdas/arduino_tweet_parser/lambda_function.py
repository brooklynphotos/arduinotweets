'''Takes a message in SQS pushed by twitter_mine and decides what to put into dynamoDB'''

import boto3
import json
from datetime import datetime

job_time_attr = 'job_time'

def lambda_handler(event, context):
  retrieval_time, tweets = retrieve_tweets(event)
  return upsert_db(tweets, retrieval_time)

def retrieve_tweets(event: dict) -> list:
    msg_body = event['Records'][0]['body']
    retrieval_time = datetime.utcnow().isoformat()
    return retrieval_time, [{'id': t['id_str'], 'text': t['text'], 'created_at': t['created_at'], 'user_id': t['user_id'], job_time_attr: retrieval_time} for t in json.loads(msg_body)['responsePayload']]

def upsert_db(tweets: list, retrieval_time: str) -> list:
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
      user_ids.add(t['user_id'])
      affected.append({k: v for k,v in t.items() if k in ['id', 'user_id']})
  with users_table.batch_writer(overwrite_by_pkeys=['id']) as batch:
    for u in user_ids:
      batch.put_item(
        Item={
          'id':u,
          job_time_attr: retrieval_time
        }
      )
  return affected