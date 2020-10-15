import boto3
import botocore
import json
import requests

BUCKET_NAME = 'gzsecretsforapps'  # replace with your bucket name
KEY = 'twitter_credentials.json'  # replace with your object key
ENDPOINT = 'https://api.twitter.com/1.1/search/tweets.json?q=%%23%s&result_type=recent'

def lambda_handler(event, context):
    project_name = event["projectName"]
    twitter_credentials = get_credentials(project_name)
    return latest_tweets(project_name, twitter_credentials)

def latest_tweets(project, credentials):
  url = ENDPOINT % project
  headers = {'Authorization': f"Bearer {credentials}"}
  fields = {'created_at', 'id_str', 'text', 'user'}
  statuses = requests.get(url, headers=headers).json()['statuses']
  top_level = [{k:v for k,v in s.items() if k in fields} for s in statuses]
  # redo user
  return [update_user(e) for e in top_level]

def update_user(tweet):
  base = {k:v for k,v in tweet.items() if k != 'user'}
  base['user_id'] = tweet['user']['id_str']
  return base

def get_credentials(project_name: str):
    s3 = boto3.client('s3')
    print(f"Reading from {BUCKET_NAME}/{KEY}")
    try:
        body = s3.get_object(Bucket=BUCKET_NAME, Key=KEY)['Body'].read().decode('utf-8')
        db = json.loads(body)
        return db[project_name]
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            return dict(msg="Not Found")
        else:
            raise
