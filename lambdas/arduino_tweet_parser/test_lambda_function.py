import unittest
import json

from lambda_function import retrieve_tweets, upsert_db

sample_data = r"""[
  {
    "created_at": "Tue Oct 13 11:48:40 +0000 2020",
    "id_str": "1315982787468554242",
    "text": "RT @chemaalonso: El lado del mal - VBooks de 0xWord en un nueva plataforma y por tiempo ilimitado @0xWord @MyPublicInbox1 #Arduino #hacking…",
    "user_id": "109488608"
  },
  {
    "created_at": "Tue Oct 13 11:01:30 +0000 2020",
    "id_str": "1315970915897937920",
    "text": "Mechanical-Digital Steel Ball Clock\n\n#arduino https://t.co/kZA6vsd8ac",
    "user_id": "1149087215802290178"
  }
]"""
sample_event = {'Records': [{
  'messageId': '1', 
  'receiptHandle': 'hd', 
  'body': '''{
    "version":"1.0",
    "timestamp":"2020-10-13T05:11:53.255Z",
    "requestContext":
      {
        "requestId":"r1",
        "functionArn":"arn:aws:lambda:eu-west-1:575798484766:function:twitter_mine:prod",
        "condition":"Success",
        "approximateInvokeCount":1
      },
      "requestPayload":{
        "projectName": "arduino" 
      },
      "responseContext":{
        "statusCode":200,
        "executedVersion":"1"
      },
      "responsePayload":
      %s
    }'''%sample_data, 
    'attributes': {'ApproximateReceiveCount': '1', 'SentTimestamp': '1602565913330', 'SenderId': 'AROAYMECDT4PIC25LWQ6Q:awslambda_63_20201012190408712', 'ApproximateFirstReceiveTimestamp': '1602565913341'}, 
    'messageAttributes': {}, 
    'md5OfBody': 'c613aa7994c47797191f954a75af561c', 
    'eventSource': 'aws:sqs', 
    'eventSourceARN': 'arn:aws:sqs:eu-west-1:575798484766:encrypted-queue', 
    'awsRegion': 'eu-west-1'
  }]
}

class TestTwitterUpdates(unittest.TestCase):

  def test_retrieve_tweets(self):
    retrieval_time, tweets = retrieve_tweets(sample_event)
    self.assertEqual(2, len(tweets))
    self.assertEqual(sorted(['id', 'user_id', 'created_at', 'text', 'job_time']), sorted(tweets[1].keys()))

  def test_upsert_db(self):
    retrieval_time, tweets = retrieve_tweets(sample_event)
    affected = upsert_db(tweets, retrieval_time)
    self.assertEqual(2, len(affected))

if __name__=='__main__':
  unittest.main()