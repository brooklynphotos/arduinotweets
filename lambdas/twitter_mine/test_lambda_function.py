import unittest
import json

from lambda_function import latest_tweets

class TestTwitterUpdates(unittest.TestCase):

  def test_latest_tweets(self):
    resp = latest_tweets('arduino', 'AAAAAAAAAAAAAAAAAAAAAAF3IQEAAAAAzhPXHL%2BFA21t9x4n8rb91LhRiU8%3D8sWe0pekN1D3aPxKSUIzC6RVyFtdEfRe38sW26JZ9oFMeCohW1')
    self.assertEqual(15, len(resp))
    print(json.dumps(resp))
    self.assertEqual(['created_at', 'id_str', 'text'], list(resp[0].keys()))

if __name__=='__main__':
  unittest.main()