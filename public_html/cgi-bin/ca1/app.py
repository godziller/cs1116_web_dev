from flask import Flask, abort, render_template, url_for, session, redirect, request,g
from forms import CreateTaskForm, LoginForm, UpdateUserForm, ViewTaskForm, RegisterForm, EditTaskForm, ViewLogsForm
from flask_session import Session
from database import get_db, close_db
from functools import wraps
from datetime import date, datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.teardown_appcontext(close_db)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.before_request
def load_logged_in_user():
    g.user = session.get("user_id", None)
    session_email = session.get("email", None)
    g.is_admin = session.get('is_admin', None) # Could use to gate admin functions 
  
    #setting databse here to simplify route functions
    db = get_db()
    
    client_ip = request.remote_addr
    endpoint = request.endpoint
    time = datetime.now()

    g.db.execute("""INSERT INTO traffic_logs (time,ip_addr,user_email,endpoint) VALUES (?,?,?,?)""",
            (time,client_ip, session_email, endpoint))
    g.db.commit()

def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return view(*args,**kwargs)
    return wrapped_view


"""
New wrapper function to protect admin only routes
"""
def admin_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.is_admin is None:
            return render_template("not_authorized.html")
        return view(*args,**kwargs)
    return wrapped_view


@app.route("/")
@app.route("/index.html")
def index():
    return redirect(url_for("login"))

"""
These next routes do the user login/register/logout functionality
"""

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        surname = form.surname.data
        print('got here')

        conflict_user = g.db.execute(
            """SELECT * FROM users 
               WHERE email = ?;""", (email,)).fetchone()

        if conflict_user is not None:
            return "Username is already taken"
        else:
            g.db.execute("""
                INSERT INTO users( password,first_name,surname,email)
                VALUES (?,?,?,?);""", 
                (generate_password_hash(password),first_name,surname,email))
            g.db.commit()
            return redirect(url_for("login"))    
    return render_template("register_form.html", form=form)
    


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = g.db.execute(
            """SELECT * FROM users 
               WHERE email = ?;""", (email,)).fetchone()     
        if user is None:   
            form.email.errors.append("email or password is incorrect")
        elif not check_password_hash(user["password"], password):
            form.password.errors.append("Username or password is incorrect")
        else:
            session.clear()
            session["user_id"] = user["user_id"]  # Set the user ID in session
            session["email"] = user["email"]    # we use this for traffic logging

            if bool(user['is_admin']) is True:
                session['is_admin'] = True
                print(' is an admin')
                print(user['is_admin'])
                print(bool(user['is_admin']))

            next_page = request.args.get("next")
            if not next_page:
                next_page = url_for("list_tasks")
            session.modified = True             # Handle any flask version issues with session object
            return redirect(next_page)
    return render_template("login_form.html", form=form)


@app.route("/logout", methods=["GET", "POST"]) 
@login_required
def logout():
    session.clear()
    return redirect( url_for("login"))



'''
This section are all task route functions
'''

@app.route("/list_tasks", methods=["GET", "POST"]) 
@login_required
def list_tasks():
    form = ViewTaskForm()
    user_id = str(session["user_id"])

    tasks = g.db.execute("""SELECT * FROM tasks WHERE user_id = ?;""", (user_id)).fetchall()
    if form.validate_on_submit():
        print('here')

        #return redirect(url_for(add_task))
    

    return render_template("view_task_form.html",tasks=tasks, form=form, caption='All Tasks')


@app.route("/todays_tasks", methods=["GET", "POST"]) 
@login_required
def todays_tasks():
    form = ViewTaskForm()
    user_id = session.get("user_id")
    today = date.today().isoformat()

    tasks = g.db.execute("""
        SELECT * FROM tasks 
        WHERE user_id = ? AND due_date = ?;
    """, (user_id, today)).fetchall()
    

    return render_template("view_task_form.html",tasks=tasks, form=form, caption='Todays Tasks')

@app.route("/this_week_tasks", methods=["GET"])
@login_required
def this_week_tasks():
    form = ViewTaskForm()
    user_id = session.get("user_id")
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())  # Monday of this week
    end_of_week = start_of_week + timedelta(days=6)          # Sunday of this week

    tasks = g.db.execute("""
        SELECT * FROM tasks 
        WHERE user_id = ? AND due_date >= ? AND due_date <= ?;
    """, (user_id, start_of_week, end_of_week)).fetchall()

    return render_template("view_task_form.html",tasks=tasks, form=form, caption='This Weeks Tasks')


@app.route("/next_week_tasks", methods=["GET"])
@login_required
def next_week_tasks():
    form = ViewTaskForm()
    user_id = session.get("user_id")
    today = date.today()
    start_of_next_week = today + timedelta(days=(7 - today.weekday()))  # Monday of next week
    end_of_next_week = start_of_next_week + timedelta(days=6)                 # Sunday of next week

    tasks = g.db.execute("""
        SELECT * FROM tasks 
        WHERE user_id = ? AND due_date >= ? AND due_date <= ?;
    """, (user_id, start_of_next_week, end_of_next_week)).fetchall()

    return render_template("view_task_form.html",tasks=tasks, form=form, caption='Next Weeks Tasks')

@app.route("/add_task", methods=["GET", "POST"]) 
@login_required
def add_task():
    form = CreateTaskForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        due_date = form.due_date.data
        priority = form.priority.data

        print('GOT HERE')
        if due_date < datetime.now().date():
            form.due_date.errors.append("Date must be in the future")
        else:
            g.db.execute("""INSERT INTO tasks (user_id,title, description, due_date, priority) VALUES (?,?,?,?,?)""",
                       (session["user_id"],title, description, due_date, priority,  ))
            g.db.commit()
            print('success')
            return redirect(url_for("list_tasks"))
    return render_template("create_task_form.html", form=form)


@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
@login_required
def edit_task(task_id):
    task = g.db.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    form = EditTaskForm()


    # Populate form fields with task details, need to catch this in the GET message
    # to make sure it does not use old data in the new submit which is a POST
    if request.method == "GET":
        form.title.data = task["title"]
        form.description.data = task["description"]
        form.due_date.data = task["due_date"]
        form.priority.data = task["priority"]
        form.status.data = task["status"]

    if request.method == "POST" and "delete" in request.form:  # Check if the delete button is pressed
        g.db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        g.db.commit()
        return redirect(url_for("list_tasks"))
    
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        due_date = form.due_date.data
        priority = form.priority.data
        status = form.status.data
        
        if due_date < datetime.now().date():
            form.due_date.errors.append("Date must be in the future")
        else:
            print(title, status, priority)
            g.db.execute("""
                UPDATE tasks 
                SET title = ?, description = ?, due_date = ?, priority = ?, status = ?
                WHERE id = ?
            """, (title, description, due_date, priority, status, task_id))
            g.db.commit()
            return redirect(url_for("list_tasks"))
        
    

    return render_template("edit_task_form.html", form=form)

"""
Routes for Special Admin Functions
"""

@app.route("/view_logs", methods=["GET", "POST"]) 
@login_required
@admin_required
def view_logs():
    form = ViewLogsForm
    logs = g.db.execute(("""SELECT * FROM traffic_logs; """)).fetchall()
    for log in logs:
        print(log["user_email"])
    return render_template("view_logs_form.html", form=form, logs=logs)


@app.route("/delete_all_logs", methods=["GET", "POST"]) 
@login_required
@admin_required
def delete_all_logs():
    form = ViewLogsForm
    g.db.execute("""DELETE FROM traffic_logs """)
    g.db.commit()
    return render_template("view_logs_form.html", form=form, logs='')


@app.route("/list_users", methods=["GET"])
@login_required
@admin_required
def list_users():

    users = g.db.execute("SELECT * FROM users").fetchall()

    return render_template("list_users.html", users=users)

@app.route("/update_user/<int:user_id>", methods=["GET", "POST"])
@login_required
@admin_required
def update_user(user_id):

    user = g.db.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
    form = UpdateUserForm()
    print("First Name")
    print(user["first_name"])   
    # Populate form fields with task details, need to catch this in the GET message
    # to make sure it does not use old data in the new submit which is a POST
    if request.method == "GET":
        print("In GET")
        form.first_name.data = user["first_name"]
        form.surname.data = user["surname"]
        form.email.data = user["email"]
        form.password.data = user["password"]
        form.is_admin.data = user["is_admin"]
  
    if request.method == "POST" and "delete" in request.form:  # Check if the delete button is pressed
        print("Deleting User")
        g.db.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
        g.db.commit()
        return redirect(url_for("list_users"))

    if form.validate_on_submit():
        # Update user data with form data
        print("In VALIDATE")
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        surname = form.surname.data
        is_admin = form.is_admin.data

        g.db.execute("""
            UPDATE users 
            SET password = ?, email = ?, first_name = ?, surname = ?, is_admin = ?
            WHERE user_id = ?
        """, (generate_password_hash(password), email, first_name, surname, is_admin, user_id))
        g.db.commit()
        return redirect(url_for("list_users"))

    return render_template("update_user_form.html", form=form)