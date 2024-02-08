from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, SelectField, RadioField
from wtforms.validators import InputRequired

class WombatForm(FlaskForm):
    #one line for each of our things in form 
    wombat = BooleanField("Does Derek like wombats?")
    submit = SubmitField("Submit")


class PizzaForm():
    topping = SelectField("Does Derek like wombats?", validators=[InputRequired()], choices=["ham","pineapple", "anchovies"])
    toppings2 = RadioField("Does Derek like wombats?", default="ham" ,choices=["ham","pineapple", "anchovies"])

    submit = SubmitField("Submit")