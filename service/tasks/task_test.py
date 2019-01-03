import celery

# Test purpose only
@celery.task()
def print_hello():
    logger = print_hello.get_logger()
    logger.info("Hello")