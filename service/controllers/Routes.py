import logging
from flask import request, Blueprint, jsonify

from service import app
from service.controllers import MessageController

bp = Blueprint('mail_service', __name__, template_folder='templates')

response = {
    'VERSION': app.config['APP_VERSION']
}

@bp.route("/save_emails", methods=["POST"])
def saveEmails():
    try:
        data       = request.json
        
        return jsonify(response)
    except Exception as e:
        logging.exception(e)
        response['MESSAGE'] = "Whoops..sorry try again later"

        # Launch alert email
        # ...

        return jsonify(response)

@bp.route("/get_emails", methods=["GET"])
def showEmails():
    response['EMAILS'] = MessageController.getEmails()
    return jsonify(response)

