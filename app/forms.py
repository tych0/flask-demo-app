from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class BandForm(Form):
    band = StringField('band', validators=[DataRequired()])
