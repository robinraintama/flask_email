from service.schemas import MessageSchema, EmailSchema
from service.models import tr_messages, tm_emails

def saveMessage(request):
    json_data = request.get_json()
    if not json_data:
        return 'No input data provided'

    try:
        data = MessageSchema

def getEmails():
    emails = tm_emails.Emails.query.all()
    return EmailSchema.all_email_schema.dump(emails).data

