import logging
from datetime import datetime

from service.schemas import MessageSchema, EmailSchema
from service.models import tr_messages, tm_emails
from service import db

def saveMessage(data):
    try:
        data['timestamp'] = convertToDateTime(data['timestamp'])
        message = tr_messages.Messages(**data)
        db.session.add(message)
        return db.session.commit()
    except Exception as e:
        logging.exception(e)
        return 'Please check your request'

def getEmails():
    emails = tm_emails.Emails.query.all()
    return EmailSchema.all_email_schema.dump(emails).data

def getMessageAtTimestamp():
    timestamp = datetime.now().time()
    messages = tr_messages.Messages.query.filter_by(timestamp=timestamp).all()
    return MessageSchema.all_message_schema.dump(messages).data

def convertToDateTime(str):
    return datetime.strptime(str, '%d %b %Y %H:%M')

