import logging
from flask import request, Blueprint, jsonify
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

from service import app
from service.controllers import MessageController

bp_mail = Blueprint('mail_service', __name__, template_folder='templates')
bp_jwt = Blueprint('jwt_service', __name__, template_folder='templates')

def get_default_response():
    return {
        'VERSION': app.config['APP_VERSION']
    }

@bp_mail.route("/save_emails", methods=["POST"])
def saveEmails():
    response = get_default_response()
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

@bp_mail.route("/get_emails", methods=["GET"])
@jwt_required
def showEmails():
    response = get_default_response()
    response['EMAILS'] = MessageController.getEmails()
    return jsonify(response)

@bp_mail.route("/check_controller", methods=["GET"])
def checkController():
    response = get_default_response()
    response['MESSAGE'] = MessageController.getMessageAtTimestamp()
    return jsonify(response)

@bp_jwt.route("/request_token_fresh", methods=["POST"])
def requestTokenFresh():
    response = get_default_response()
    try:
        data = request.json
        username = data['username']
        if username:
            response['ACCESS_TOKEN'] = create_access_token(identity=username, fresh=True)
            response['REFRESH_TOKEN'] = create_refresh_token(username)
            response['MESSAGE'] = 'Here is your token'
        else:
            response['MESSAGE'] = 'Check your payload'
        return jsonify(response)
    except Exception as e:
        logging.exception(e)
        response['MESSAGE'] = 'Packman eats our code, sigh!'
        return jsonify(response)

        

