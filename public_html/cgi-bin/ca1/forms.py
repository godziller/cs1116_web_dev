from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField,  IntegerField, DecimalField, DateField
from wtforms.validators import InputRequired

class create_task_form(FlaskForm):

    submit = SubmitField("Submit")
    description = StringField("Plaintext:", validators=[InputRequired()])
    dueDate = DateField()
    importance = SelectField()
    submit = SubmitField("add")

class login_form(FlaskForm):

    firstName = StringField('Your first name: ', validators=[InputRequired()])
    surname = StringField('Your surname: ', validators=[InputRequired()])
    email = StringField('Your email: ', validators=[InputRequired()])
    password = StringField('password: ', validators=[InputRequired()])

class logout_form(FlaskForm):
    logout = SelectField('Logout')

class view_task_form(FlaskForm):
    message = StringField()
    