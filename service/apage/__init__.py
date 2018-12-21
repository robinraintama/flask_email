from flask import Blueprint

apage = Blueprint('apage', __name__)

from . import views