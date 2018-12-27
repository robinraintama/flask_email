from flask import render_template, jsonify

from . import apage
from service.controllers import MessageController

from .forms import MotivationEmailForm

@apage.route('/', methods=["GET"])
def apageIndex():
    form = MotivationEmailForm()
    request = {}
    if form.validate_on_submit():
        request['email_subject'] = form.subject.data
        request['email_content'] = form.content.data
        request['datetime'] = form.datetime.data
        response = MessageController.sendEmail(jsonify(request))
        if response is None:
            return 'Cool, its submitted'
        else:
            # Next show error on template
            return 'Not cool, it is life. Lets try again'
    
    return render_template('apage.html', form=form, title="SMERT")