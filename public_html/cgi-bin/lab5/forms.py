from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import InputRequired, NumberRange

class GuessForm(FlaskForm):

    guess = IntegerField('Guess a number between 1-100', 
                         validators=[InputRequired(message="Please enter a number"), 
                                     NumberRange(min=1, max=100, message="Keep it between the ditches!!")])
    submit = SubmitField("Submit")

