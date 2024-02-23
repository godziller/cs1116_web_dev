from flask import Flask, render_template, url_for, session, redirect
from flask_session import Session
from forms import GuessForm
from random import randint

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

    
@app.route("/guess", methods=["GET","POST"])
def guess():
    if "secret_number" not in session:
        session["secret_number"] = randint(1,100)
        print(session)
    
    friend_number = session["secret_number"]
    print(type(friend_number))
    print(friend_number)
    msg = ""

    form = GuessForm()

    if form.validate_on_submit():
        guess = form.guess.data
        print (guess)

        if guess > friend_number:
            msg = "Too high, guess again"
        elif guess < friend_number:
            msg = "Too low, guess again"
        else:
            msg = "Correct - well done"
            session.pop("secret_number")
    return render_template("guess_form.html", form=form, message = msg)
            