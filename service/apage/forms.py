from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired

from service.models import tr_messages

class MotivationEmailForm(FlaskForm):
    eventId = StringField('event id', validators=[DataRequired()])
    subject = StringField('subject', validators=[DataRequired()])
    content = StringField('content', validators=[DataRequired()])
    datetime = StringField('datetime', validators=[DataRequired()])
    submit = SubmitField('Submit')