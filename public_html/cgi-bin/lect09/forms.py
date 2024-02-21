from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, SelectField, RadioField, DateField
from wtforms.validators import InputRequired

class GigFOrm(FlaskForm):
    band = StringField()
    gig_date = DateField()
    submit = SubmitField()