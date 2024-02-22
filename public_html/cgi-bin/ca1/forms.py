from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField,  IntegerField, DecimalField, DateField
from wtforms.validators import InputRequired

class todo_form(FlaskForm):

    submit = SubmitField("Submit")
    description = StringField("Plaintext:", validators=[InputRequired()])
    dueDate = DateField()
    importance = SelectField()

    