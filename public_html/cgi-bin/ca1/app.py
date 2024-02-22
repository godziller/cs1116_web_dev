from flask import Flask, render_template, url_for, session, redirect
from forms import create_task_form, login_form, logout_form, view_task_form
from flask_session import Session
from database import get_db, close_db


app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"

'''
This section are all user login route functions
'''

# @app.route("/register", methods=["GET", "POST"]) TODO:
# def register():

# @app.route("/login", methods=["GET", "POST"]) TODO:
# def login():

# @app.route("/logout", methods=["GET", "POST"]) TODO:
# def logout():

# @app.route("/unsubscribe", methods=["GET", "POST"]) TODO:
# def unsubscribe():


'''
This section are all task route functions
'''

@app.route("/list_tasks", methods=["GET", "POST"]) #TODO:
def list_tasks():
    form = view_task_form()
    return render_template("view_task_form.html", form=form)


# @app.route("/update_task", methods=["GET", "POST"]) TODO:
# def update_task():

# @app.route("/delete_task", methods=["GET", "POST"]) TODO:
# def delete_task():

@app.route("/add_task", methods=["GET", "POST"]) #TODO:
def add_task():
    form = create_task_form()
    return render_template("create_task_form.html", form=form)


# @app.route("/get_upcoming_tasks", methods=["GET", "POST"]) TODO:
# def get_upcoming tasks():
# for today, for this week, for time window?


'''
this section are all project route functions
'''
#@app.route("/add_project", methods=["GET", "POST"]) #TODO:
#def add_project():
#    form = todo_form()
#    return render_template("todo_form.html", form=form)


# @app.route("/delete_project", methods=["GET", "POST"]) TODO:
# def delete_project():

# @app.route("/list_projects", methods=["GET", "POST"]) TODO:
# def list_projects():

'''
This section are all admin special functions
'''

# @app.route("/adminlogin", methods=["GET", "POST"]) TODO:
# def adminlogin():

# @app.route("/update_admin_password, methods=["GET", "POST"]) TODO:
# def update_admin_password():
