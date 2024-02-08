from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class BMIForm(FlaskForm):
    #one line for each of our things in form 
    weight = DecimalField("weigh (kg)", validators=[InputRequired(),NumberRange(10,100)])
    height = DecimalField("height (m)", validators=[InputRequired(), NumberRange(0.5,2.5)])
    bmi = DecimalField("bmi")
    submit = SubmitField("submit")
