import os, logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
import celeryconfig

from flask_bootstrap import Bootstrap

# Initialize Flask and config
app = Flask(__name__)
app.config.from_pyfile('../config.py')

# Initialize MYSQL/MARIADB connection
db = SQLAlchemy(app)
# app.app_context().push()

# Initialize bBootstrap
Bootstrap(app)

# Initialize Log
basedir = os.path.abspath(os.path.dirname(__file__))
LOG_FILENAME = basedir+'/log/error.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.ERROR)

# Initialize Celery
def make_celery(app):
    # create context tasks in celery
    celery = Celery(
        app.import_name,
        broker=app.config['BROKER_URL']
    )
    celery.conf.update(app.config)
    celery.config_from_object(celeryconfig)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    
    celery.Task = ContextTask

    return celery

celery = make_celery(app)

from service.models import *
from service.controllers import *
from service.apage import apage

# Register blueprint for GUI(form) and API
app.register_blueprint(Routes.bp, url_prefix="/api")
app.register_blueprint(apage, url_prefix="/form")

# Welcoming message
# Quick check to make sure your flask is working
@app.route('/')
def index():
    return 'Welcome welcome welcome'