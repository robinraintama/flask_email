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
        # Convert timestamp string to general datetime format
        data['timestamp'] = convertToDateTime(data['timestamp'])

        # Timestamp should be greater than now
        if data['timestamp'] > datetime.now():
                # Get delta time in seconds
                delaySeconds = getSecondsDifference(data['timestamp'])

                # Save message to database
                message = tr_messages.Messages(**data)
                db.session.add(message)

                arEmails = list()
                emails = getEmails()
                for email in emails:
                        arEmails.append(email['email'])
                print(arEmails, data["email_subject"], data["email_content"]) 

                # Call email task asynchronously
                # ARGS = Email addreses, subject, content
                # Countdown = delta time in seconds
                email_users.apply_async(args=[arEmails, data["email_subject"], data["email_content"]], countdown=delaySeconds)

                # Commit db transaction
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
    messages = tr_messages.Messages.query.all()
    return MessageSchema.all_message_schema.dump(messages).data

def getSecondsDifference(dt):
        dtDelta = (dt - datetime.now()).total_seconds()
        return int(dtDelta)

# Send email function with SMTP
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

