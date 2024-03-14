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


"""
The application has two types of users - a regular user and an admin user.
Use the register function to register as a new user.

For admin user - the username is Admin and password Admin

The Admin can do everything a regular user can, but has more admin type functions available

Derek - I created a user account for you derek@ucc.ie and password is derek - this is set as a regular
user - but you have access to admin account too - so hope that's ok :-) If not - you can always 
promote youself to admin which is a feature of an admin user.

Once registered as a regular user, you login using your email and password. Emails are unique and from 
experience is the typical identification used on the web - hence this is the adopted approach.

Of note - I took inspiration from class lecture for login_required and created my own to control
access to admin type functions - you can test these by copying a url as admin, log in as regular user
and past and try get access - the response should indicate access if forbidden.

I also took advantage of the 'before_request' to catch all traffic logs to collect simple data
for web traffic which you can look at as admin user.

I used learned lessons from lecture on session object to allow me to know if a logged in user is 
of type admin or not.

I have included some simple py files that helped me understand how to get 'this week' and next week 
data for db searchs - you can take a look if interested - weekday_hack.py - and run it as a standard 
python app.

Also a very basic hack to get me the hash of the Admin passowrd is included to help me get a proper
sql insert to setup my todo.db with an admin user for convienence.

I've done my best to comment the code so it is understandable, but did not over do it for simple stuff.
I purposfully left some of my debug print statements in the code that helped me with the project, but
I thought it might be handy for you running the code to see what's happening.

"""

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
    g.db.commit()   # note i use the global g.db, for cleanliness throughout the file 

"""
setting up the login required function to be used before most of my routes 
"""
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
Note - most websites use email as unique identifier, so we follow this common pattern here.
"""

@app.route("/register", methods=["GET", "POST"]) 
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        password = form.password.data
        confirm_password = form.confirm_password.data
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
            if form.password.data == form.confirm_password.data:
                g.db.execute("""
                    INSERT INTO users( password,first_name,surname,email)
                    VALUES (?,?,?,?);""", 
                    (generate_password_hash(password),first_name,surname,email))
                g.db.commit()
                return redirect(url_for("login"))   
            else:
                form.password.errors.append("both passwords must be the same")


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
            form.password.errors.append("email or password is incorrect")
        else:
            session.clear()
            session["user_id"] = user["user_id"]  # Set the user ID in session
            session["email"] = user["email"]    # we use this for traffic logging

            if bool(user['is_admin']) is True:  #checking if our sql is_admin variable is a 1 or 0, true or false. i cast it to a bool for use in python
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
        print('here')   #useless function used as a milestone test. ignore but to acknowledge progress


    return render_template("view_task_form.html",tasks=tasks, form=form, caption='All Tasks')


@app.route("/todays_tasks", methods=["GET", "POST"]) 
@login_required
def todays_tasks():
    form = ViewTaskForm()
    user_id = session.get("user_id")
    today = date.today()   #finding the current date to create a function that gets tasks in a range (tasks today)

    tasks = g.db.execute("""
        SELECT * FROM tasks 
        WHERE user_id = ? AND due_date = ?;
    """, (user_id, today)).fetchall()
    

    return render_template("view_task_form.html",tasks=tasks, form=form, caption='Todays Tasks')


"""
Calculating this and next week.
date.today() learned in lecture/labs. Then needed to figure out how to create a start and end week
marker to query the db.

Loads of info, but the key to understanding was - https://docs.python.org/3/library/datetime.html#timedelta-objects

Which if I understood correctly, turns a 'day' into its own type, which you can do simple +/- on.
A bit of hacking and experimenting got me the following 2 pieces of code which work well.

"""
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
        if due_date < datetime.now().date():    #check to see if date is beyond the current
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
def update_user(user_id): #TODO: Need to check password and 2nd password are the same.

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