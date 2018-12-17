import logging
import celery
import app
from service.controllers import MessageController

@celery.task
def email_users(email, subject, message):
    logger.info("email_users called")
    try:
        with app.app_context():
            MessageController.sendEmail(email, subject, message)
            logger.info("Success {}".format(mail['email']))
    
    except Exception as e:
        logging.exception(e)
        logger.info(e)