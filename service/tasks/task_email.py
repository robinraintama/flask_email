import celery
from service.controllers import MessageController

@celery.task()
def email_users():
    emails = MessageController.getEmails()
    messages = MessageController.getMessageAtTimestamp()

    logger = email_users.get_logger()
    logger.info(messages)