from flask import Blueprint

# Setup blueprint for "a page"
# Simple GUI to send email with delay
apage = Blueprint('apage', __name__)

from . import views