from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField,  IntegerField, DecimalField, DateField
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
    user_id = StringField("User id: ", validators=[InputRequired()])
    password = StringField("Password: ", validators=[InputRequired()])
    password2 = StringField("Repeat Password: ", validators=[InputRequired()])    
    submit = SubmitField("Register")
