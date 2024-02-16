from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, SelectField, RadioField
from wtforms.validators import InputRequired

class winnerForm(FlaskForm):
    country = StringField('Country:', validators=[InputRequired()])
    submit = SubmitField()

class minWinner(FlaskForm):
    country = StringField('Country')
    submit = SubmitField()
    points = StringField('Points')
