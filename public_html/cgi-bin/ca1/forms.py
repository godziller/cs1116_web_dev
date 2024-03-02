from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField,  IntegerField, DecimalField, DateField, PasswordField
from wtforms.validators import InputRequired

class create_task_form(FlaskForm):

    submit = SubmitField("Submit")
    description = StringField("Plaintext:", validators=[InputRequired()])
    dueDate = DateField()
    importance = SelectField("Importance:", choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], validators=[InputRequired()])
    submit = SubmitField("add")
    

class login_form(FlaskForm):
    user_id = StringField("User id: ", validators=[InputRequired()])
    password = StringField("Password: ", validators=[InputRequired()])
    submit = SubmitField("Log In")


class logout_form(FlaskForm):
    logout = SelectField('Logout')

class view_task_form(FlaskForm):
    message = StringField()
    

class register_form(FlaskForm):
    password = PasswordField("Password: ", validators=[InputRequired(message='password')])
    confirm_password = PasswordField("Confirm Password: ", validators=[InputRequired()])
    email = StringField("Email: ", validators=[InputRequired()])
    first_name = StringField("First Name: ", validators=[InputRequired()])
    surname = StringField("Surname: ", validators=[InputRequired()])
    submit = SubmitField("Register")