from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField

class VoteForm(FlaskForm):
    vote = RadioField("What is your favourite binary number?",
        choices= ["0","1"],
        default="0")
    submit = SubmitField("Submit")
