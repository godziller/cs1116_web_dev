from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField,  IntegerField, DecimalField, DateField, PasswordField
from wtforms.validators import InputRequired

class create_task_form(FlaskForm):

    title = StringField("Title: ", validators=[InputRequired()])
    description = StringField("Description:", validators=[InputRequired()])
    due_date = DateField()
    priority = SelectField("Priority:", choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], validators=[InputRequired()])
    submit = SubmitField("add")
    

class login_form(FlaskForm):
    email = StringField("Email: ", validators=[InputRequired()])
    password = PasswordField("Password: ", validators=[InputRequired()])
    submit = SubmitField("Log In")


class logout_form(FlaskForm):
    logout = SelectField('Logout')


class view_task_form(FlaskForm):
    add_task = SubmitField("Add Task")
    

class register_form(FlaskForm):
    password = PasswordField("Password: ", validators=[InputRequired(message='password')])
    confirm_password = PasswordField("Confirm Password: ", validators=[InputRequired()])
    email = StringField("Email: ", validators=[InputRequired()])
    first_name = StringField("First Name: ", validators=[InputRequired()])
    surname = StringField("Surname: ", validators=[InputRequired()])
    submit = SubmitField("Register")

class edit_task_form(FlaskForm):
    title = StringField("Title: ", validators=[InputRequired()])
    description = StringField("Description:", validators=[InputRequired()])
    due_date = DateField()
    priority = SelectField("Priority:", choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], validators=[InputRequired()])
    status = SelectField("Status", choices=[('New', 'New'), ('In Progress', 'In Progress'), ('Done', 'Done'), ('Abandoned', 'Abandoned')], validators=[InputRequired()])

    submit = SubmitField("update")
    delete = SubmitField("Delete")

class view_logs_form(FlaskForm):
    delete_logs = SubmitField("Delete Logs")


class update_user_form(FlaskForm):
    first_name = StringField("First Name: ", validators=[InputRequired()])
    surname = StringField("Surname: ", validators=[InputRequired()])
    email = StringField("Email: ", validators=[InputRequired()])
    password = PasswordField("Password: ", validators=[InputRequired(message='password')])
    confirm_password = PasswordField("Confirm Password: ", validators=[InputRequired()])
    is_admin = SelectField("IS ADMIN", choices=[(0, "FALSE"), (1, "TRUE")])
    submit = SubmitField("Update")