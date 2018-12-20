import logging
from datetime import datetime
from flask import request
from flask_mail import Mail, Message

from service.schemas import MessageSchema, EmailSchema
from service.models import tr_messages, tm_emails
from service import db, app
from service.tasks.task_email import email_users

def saveMessage(data):
    try:
        data['timestamp'] = convertToDateTime(data['timestamp'])
        if data['timestamp'] > datetime.now():
                delaySeconds = getSecondsDifference(data['timestamp'])
                message = tr_messages.Messages(**data)
                db.session.add(message)

                arEmails = list()
                emails = getEmails()
                for email in emails:
                        arEmails.append(email['email'])
                print(arEmails, data["email_subject"], data["email_content"]) 
                email_users.apply_async(args=[arEmails, data["email_subject"], data["email_content"]], countdown=delaySeconds)

                return db.session.commit()
        else:
                return 'Check your datetime'
    except Exception as e:
        logging.exception(e)
        return 'Please check your request'

def getEmails():
    emails = tm_emails.Emails.query.all()
    return EmailSchema.all_email_schema.dump(emails).data

def getMessageAtTimestamp():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
#     messages = tr_messages.Messages.query.filter_by(timestamp=timestamp).all()
    messages = tr_messages.Messages.query.all()
    return MessageSchema.all_message_schema.dump(messages).data

def getSecondsDifference(dt):
        return (dt - datetime.now().timestamp())

def sendEmail(email_addresses, subject, message):
        print(email_addresses, subject, message)

        try:
                mail            = Mail(app)
                msg             = Message(subject, sender=(app.config['MAIL_SENDER'], app.config['MAIL_USERNAME']), recipients=email_addresses)
                msg.body        = message
                response        = mail.send(msg)
                logging.info(response)
                return 'success'

        except Exception as e:
                logging.exception("Email error")
                return 'failed'

        # return request.post(
        #         "https://api.mailgun.net/v3/{}/messages".format(app.config['MAIL_DOMAIN']),
        #         auth=("api", app.config['MAIL_API_KEY']),
        #         data={"from": "{}} <mailgun@{}}>".format(app.config['MAIL_SENDER'], app.config['MAIL_DOMAIN']),
        #                 "to": [email_address],
        #                 "subject": subject,
        #                 "text": message}
        # )

def convertToDateTime(str):
    return datetime.strptime(str, '%d %b %Y %H:%M')

