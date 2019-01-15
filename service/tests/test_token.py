import unittest
import json
from flask_jwt_extended import get_jwt_identity, decode_token
import jwt

from service import app
from service.controllers import TokenController

class TokenTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def requestToken(self, body_request, content_type='application/json', raw=False, fresh=False):
        if fresh:
            url = 'jwt/request_token'
        else:
            url = 'jwt/request_token_fresh'
        with self.app as app:
            response = app.post(
                url,
                data = json.dumps(body_request),
                content_type=content_type
            )
            if raw:
                data = response
            else:
                data = json.loads(response.data.decode())
        return data

    def getEmail(self, headers):
        with self.app as app:
            response = app.get(
                '/api/get_emails',
                headers=headers
            )
            data = json.loads(response.data.decode())
        return data

    def test_request_token_fresh(self):
        body_request = {
            "username": 1
        }

        data = self.requestToken(body_request, fresh=True)

        if data['ACCESS_TOKEN'] and data['REFRESH_TOKEN']:
            self.access_token = data['ACCESS_TOKEN']
            self.refresh_token = data['REFRESH_TOKEN']

        self.assertTrue(self.access_token)
        self.assertTrue(self.refresh_token)

    def test_request_token(self):
        body_request = {
            "username": 1
        }

        data = self.requestToken(body_request)

        if data['ACCESS_TOKEN'] and data['REFRESH_TOKEN']:
            self.access_token = data['ACCESS_TOKEN']
            self.refresh_token = data['REFRESH_TOKEN']

        self.assertTrue(self.access_token)
        self.assertTrue(self.refresh_token)

    def test_show_emails(self):
        body_request = {
            "username": 1
        }

        data = self.requestToken(body_request)

        headers = {
            "Authorization" : "Bearer " + data['ACCESS_TOKEN']
        }

        data = self.getEmail(headers)
        self.assertTrue(len(data['EMAILS']) > 0)