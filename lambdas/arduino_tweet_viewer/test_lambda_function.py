import unittest
import json

from lambda_function import get_user, get_users

class TestTwitterUpdates(unittest.TestCase):

  def test_get_users(self):
    users_resp = get_users()
    self.assertEqual(200, users_resp['statusCode'])
    users = users_resp['body']
    self.assertEqual(10, len(users))
    self.assertEqual('284068570', users[0])

  def test_get_user_success(self):
    user = get_user('284068570')
    self.assertEqual(200, user["statusCode"])

  def test_get_user_notfoud(self):
    user = get_user('123')
    self.assertEqual(404, user["statusCode"])

if __name__=='__main__':
  unittest.main()