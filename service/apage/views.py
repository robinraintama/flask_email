from flask import render_template, jsonify

from . import apage
from service.controllers import MessageController

from .forms import MotivationEmailForm

@apage.route('/', methods=["GET", "POST"])
def apageIndex():
    form = MotivationEmailForm()
    request = {}
    if form.validate_on_submit():
        request['event_id'] = form.eventId.data
        request['email_subject'] = form.subject.data
        request['email_content'] = form.content.data
        request['timestamp'] = form.datetime.data
        response = MessageController.saveMessage(request)
        if response is None:
            return 'Cool, its submitted'
        else:
            # Next show error on template
            return response
    
    return render_template('apage.html', form=form, title="SMERT")