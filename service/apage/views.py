from flask import render_template

from service import apage
from forms import MotivationEmailForm

@apage.route('/')
def apageIndex():
    form = MotivationEmailForm()

    return render_template('apage/index.html', form=form, title="SMERT")