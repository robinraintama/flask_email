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
    if request.content_type == 'application/json':
        try:
            data       = request.json
            result = MessageController.saveMessage(data)
            if result is None:
                response['MESSAGE'] = "SUCCESS"
            else:
                response['MESSAGE'] = result
        except Exception as e:
            logging.exception(e)
            response['MESSAGE'] = "Whoops..sorry try again later"

            # Launch alert email
            MessageController.sendEmail("robinraintama@gmail.com", "ERROR: Save Emails", e)
    else:
        response['MESSAGE'] = "Send your request with JSON format"
    
    return jsonify(response)

@bp.route("/get_emails", methods=["GET"])
def showEmails():
    response['EMAILS'] = MessageController.getEmails()
    return jsonify(response)

@bp.route("/check_controller", methods=["GET"])
def checkController():
    response['MESSAGE'] = MessageController.getMessageAtTimestamp()
    return jsonify(response)

