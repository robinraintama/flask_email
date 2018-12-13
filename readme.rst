Description
==========
Straight forward project to implement web services + celery scheduler and task

How to Run Scheduler
----------

- **Test Task**
    Run scheduler
.. venv/bin/celery beat -A service.celery --schedule=/tmp/celerybeat-schedule --loglevel=INFO --pidfile=/tmp/celerybeat.pid

    Run task
.. venv/bin/celery worker -A service.celery --loglevel=INFO

- **Email Task**
    ???