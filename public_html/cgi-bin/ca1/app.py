from flask import Flask, render_template, url_for, session, redirect, request,g
from forms import create_task_form, login_form, logout_form, view_task_form, register_form
from flask_session import Session
from database import get_db, close_db
from functools import wraps
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

'''
This section are all user login route functions
'''
@app.before_request
def load_logged_in_user():
    g.user = session.get("user_id", None)
    #All functions need db, so moving here to clean up route code
    g.db = get_db()


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return view(*args,**kwargs)
    return wrapped_view


@app.route("/register", methods=["GET", "POST"])
def register():
    form = register_form()

    if form.validate_on_submit():
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        surname = form.surname.data
        print('got here')

        conflict_user = db.execute(
            """SELECT * FROM users 
               WHERE email = ?;""", (email,)).fetchone()

        if conflict_user is not None:
            return "Username is already taken"
        else:
            print('here')
            db.execute("""
                INSERT INTO users(user_id, password,first_name,surname,email)
                VALUES (?,?,?,?,?);""", 
                (user_id, generate_password_hash(password),first_name,surname,email))
            db.commit()
            return redirect(url_for("login"))    
    return render_template("register_form.html", form=form)
    
    
@app.route("/login", methods=["GET", "POST"])
def login():
    form = login_form()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = db.execute(
            """SELECT * FROM users 
               WHERE email = ?;""", (email,)).fetchone()     
        if user is None:   
            form.email.errors.append("email or password is incorrect")
        elif not check_password_hash(user["password"], password):
            form.password.errors.append("Username or password is incorrect")
        else:
            session.clear()
            session["user_id"] = user["user_id"]  # Set the user ID in session
            next_page = request.args.get("next")
            if not next_page:
                next_page = url_for("list_tasks")
            return redirect(next_page)
    return render_template("login_form.html", form=form)


@app.route("/logout", methods=["GET", "POST"]) 
def logout():
    session.clear()
    return redirect( url_for("register"))

# @app.route("/unsubscribe", methods=["GET", "POST"]) TODO:
# def unsubscribe():


'''
This section are all task route functions
'''

@app.route("/list_tasks", methods=["GET", "POST"]) #TODO:
def list_tasks():
    form = view_task_form()
    user_id = str(session["user_id"])

    tasks = db.execute("""SELECT * FROM tasks WHERE user_id = ?;""", (user_id)).fetchall()
    if form.validate_on_submit():
        print('here')

        #return redirect(url_for(add_task))
    

    return render_template("view_task_form.html",tasks=tasks, form=form, caption='Upcoming Tasks')

    


# @app.route("/update_task", methods=["GET", "POST"]) TODO:
# def update_task():

# @app.route("/delete_task", methods=["GET", "POST"]) TODO: 
# def delete_task():

@app.route("/add_task", methods=["GET", "POST"]) #TODO:
@login_required
def add_task():
    form = create_task_form()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        due_date = form.dueDate.data
        importance = form.importance.data
        print('GOT HERE')
        if due_date <= datetime.now().date():
            form.dueDate.errors.append("Date must be in the future")
        else:
            db.execute("""INSERT INTO tasks (user_id,title, description, due_date, priority) VALUES (?,?,?,?,?)""",
                       (session["user_id"],title, description, due_date, importance ))
            db.commit()
            print('success')
            return redirect(url_for("list_tasks"))
    return render_template("create_task_form.html", form=form)


'''

@app.route("/get_upcoming_tasks", methods=["GET", "POST"]) #TODO:
def get_upcoming_tasks():
# for today, for this week, for time window?
    form = view_task_form()




    return render_template("view_task_form.html", form=form, tasks=tasks, caption='Upcoming Tasks')
'''

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
