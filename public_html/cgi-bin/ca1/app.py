from flask import Flask, render_template, url_for, session, redirect, request
from forms import create_task_form, login_form, logout_form, view_task_form, register_form
from flask_session import Session
from database import get_db, close_db
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

'''
This section are all user login route functions
'''

@app.route("/register", methods=["GET", "POST"])
def register():
    form = register_form()
    if form.validate_on_submit():
        print('HERE ')

        
    

       

    return render_template('register_form.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = login_form()
    if form.validate_on_submit():
        user_id = form.user_id.data
        password = form.password.data
        db = get_db()
        user = db.execute(
            """SELECT * FROM users 
               WHERE user_id = ?;""", (user_id,)).fetchone()     
        if user is None:   
            form.user_id.errors.append("Username or password is incorrect")
        elif not check_password_hash(user["password"], password):
            form.password.errors.append("Username or password is incorrect")
        else:
            session.clear()
            session["user_id"] = user_id
            next_page = request.args.get("next")
            if not next_page:
                next_page = url_for("index")
            return redirect(next_page)
    return render_template("login_form.html", form=form)


@app.route("/logout", methods=["GET", "POST"]) 
def logout():
    session.clear()
    return redirect( url_for("index"))

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


@app.route("/get_upcoming_tasks", methods=["GET", "POST"]) #TODO:
def get_upcoming_tasks():
# for today, for this week, for time window?
    form = view_task_form()
    db = get_db()
    tasks = db.execute("""SELECT * FROM tasks;""").fetchall()
 
    return render_template("view_task_form.html", form=form, tasks=tasks, caption='Upcoming Tasks')


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
