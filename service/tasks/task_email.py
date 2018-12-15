import logging
import celery
from service.controllers import MessageController

@celery.task()
def email_users():
    emails = MessageController.getEmails()
    messages = MessageController.getMessageAtTimestamp()

    logger = email_users.get_logger()
    logger.info(messages)
    logger.info(emails)

    try:
        for message in message:
            for user in users:
                MessageController.sendEmail(user.email_address, message.subject, message.message)
    
    except Exception as e:
        logging.exception(e)
        logger.info(e)