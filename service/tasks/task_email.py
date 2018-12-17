import logging
import celery
import app
from flask import request
from service.controllers import MessageController

@celery.task()
def email_users():
    emails = MessageController.getEmails()
    messages = MessageController.getMessageAtTimestamp()

    logger = email_users.get_logger()
    logger.info(messages)
    logger.info(emails)

    connect_timeout, read_timeout = 5.0, 30.0

    try:
        for message in messages:
            for mail in emails:
                with MessageController.sendEmail(mail['email'], message['email_subject'], message['email_content']):
                    logger.info("Success {}".format(mail['email']))
    
    except Exception as e:
        logging.exception(e)
        logger.info(e)

def sendEmail(email_address, subject, message):
    return request.post(
        "https://api.mailgun.net/v3/{}/messages".format(app.config['MAIL_DOMAIN']),
        auth=("api", app.config['MAIL_API_KEY']),
        data={"from": "{}} <mailgun@{}}>".format(app.config['MAIL_SENDER'], app.config['MAIL_DOMAIN']),
              "to": [email_address],
              "subject": subject,
              "text": message},
        timeout = (5.0, 30.0))