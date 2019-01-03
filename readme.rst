Description
==========
Straight forward project to implement web services + celery scheduler and task

Flask setup
----------

- Virtualenv setup and activate
- Pip install -r requirements.txt
- Fill and rename config_example.py to config.py
- flask run

How to test
----------

Run
.. node2

How to Run Scheduler
----------

- Email Task
    Run task
    venv/bin/celery worker -A service.celery --loglevel=INFO

Routes Access
----------

- Form
    [domain]:[PORT]/form
    ex:
    http://localhost:5000/form/

- API
    [domain]:[PORT]/api/save_emails
    **POST**
    content_type = 'application/json'
    body = 
    {
        "event_id":"",
        "email_subject":"",
        "email_content":"",
        "timestamp":"",
    }