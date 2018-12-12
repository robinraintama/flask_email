import unittest
import os
import json
from operator import getitem

from service import app

class MailTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_add_email_non_json(self):
        body_request = {
            "event_id": 1,
            "email_subject": "NON JSON",
            "email_content": "TEXT TYPE",
            "timestamp": "1 Jan 2019 10:10"
        }

        with self.app as app:
            response = app.post(
                'api/save_emails',
                data = json.dumps(body_request),
                content_type='text'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['MESSAGE'], 'Send your request with JSON format')

    def test_add_email(self):
        body_request = {
            "event_id": 1,
            "email_subject": "NON JSON",
            "email_content": "TEXT TYPE",
            "timestamp": "1 Jan 2019 10:10"
        }

        with self.app as app:
            response = app.post(
                'api/save_emails',
                data = json.dumps(body_request),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)

            # Add more assert from response
            keyInside = False
            for key in ['VERSION', 'MESSAGE']:
                keyInside = key in data
                if keyInside and key == 'VERSION':
                    self.assertTrue(data['VERSION'] == 'v0.1')
                elif keyInside and key == 'MESSAGE':
                    self.assertTrue(data['MESSAGE'] == 'SUCCESS')
                else:
                    break

            self.assertTrue(keyInside)