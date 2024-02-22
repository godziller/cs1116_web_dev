from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, RadioField, IntegerField, DecimalField
from wtforms.validators import InputRequired

class shift_form(FlaskForm):

    submit = SubmitField("Submit")
    plainText = StringField("Plaintext:", validators=[InputRequired()])
    shift = IntegerField('Shift', validators=[InputRequired()])
    cipherText = StringField("Ciphertext:")


class conversion_form(FlaskForm):
    base = RadioField(choices=['Fahrenheit', 'Celsius', 'Kelvin'], default='Fahrenheit')
    baseValue = IntegerField(validators=[InputRequired()])  

    output = RadioField(choices=['Fahrenheit', 'Celsius', 'Kelvin'], default='Fahrenheit')
    outValue = IntegerField()
    
    submit = SubmitField()

    error = StringField()

    