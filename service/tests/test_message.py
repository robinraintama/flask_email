import unittest
import os
import json
from operator import getitem

from service import app

class MailTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_add_email(self):
        body_request = {
            'event_id': 1,
            'email_subject': '',
            'email_content': '',
            'timestamp': ''
        }

        with self.app as app:
            response = app.post(
                'api/save_emails',
                data = json.dumps(body_request)
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)

            # Add more assert from response
            keyInside = 'VERSION' in data
            if keyInside:
                self.assertTrue(data['VERSION'] == 'v0.1')

            self.assertTrue(keyInside)