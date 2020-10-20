import unittest
import json

from lambda_function import get_tweets, build_rest_response

class TestUserTweets(unittest.TestCase):

  def test_get_tweets(self):
    user_id = "284068570"
    tweets = get_tweets(user_id)
    self.assertEqual(4, len(tweets))
    self.assertEqual('1316173068247732224', tweets[0])

  def test_build_rest_response_correct(self):
    items = [1,2]
    rest_resp = build_rest_response(items)
    self.assertEqual(200, rest_resp['statusCode'])

  def test_build_rest_response_missing(self):
    items = []
    rest_resp = build_rest_response(items)
    self.assertEqual(404, rest_resp['statusCode'])

if __name__=='__main__':
  unittest.main()