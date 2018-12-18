from os import environ

DEBUG                   = True
APP_VERSION             = 'v0.1'

# Database
## MYSQL
DB_HOST                 = 'localhost'
DB_USERNAME             = 'username'
DB_PASSWORD             = 'password'
DB_NAME                 = 'db_name'

## REDIS
REDIS_HOST              = '127.0.0.1'
REDIS_PORT              = 6379
BROKER_URL              = environ.get('REDIS_URL', "redis://{host}:{port}/0".format(host=REDIS_HOST, port=str(REDIS_PORT)))

# SQLALCHEMY
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME)
JSON_SORT_KEYS          = False

# Celery
CELERY_RESULT_BACKEND   = BROKER_URL

# EMAIL
## MAILGUN
MAIL_API_KEY            = 'api_key'
MAIL_DOMAIN             = 'https:mail.domain.com/endpoint'
MAIL_SERVER             = 'smtp.email.com'
MAIL_SENDER             = 'Sender'
#MAIL_USERNAME          = ''
#MAIL_PASSWORD          = ''
#MAIL_PORT              = 587
#MAIL_USE_SSL           = False
MAIL_USE_TLS            = True