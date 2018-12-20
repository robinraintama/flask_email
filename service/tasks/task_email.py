import logging
import celery
from service import app
from service.controllers import MessageController

@celery.task
def email_users(email, subject, message):
    logger = email_users.get_logger()
    logger.info("email_users called")
    try:
        with app.app_context():
            response = MessageController.sendEmail(email, subject, message)
            logger.info("Success {}".format(response))
    
    except Exception as e:
        logging.exception(e)
        logger.info(e)