from celery.schedules import crontab
from pytz import timezone

CELERY_IMPORTS = ('service.tasks.task_test')
CELERY_TASK_RESULT_EXPIRES = 30
CELERY_TIMEZONE = 'UTC'

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULE = {
    'test-celery': {
        'task': 'service.tasks.task_test.print_hello',
        'schedule': crontab(10)
    }
}