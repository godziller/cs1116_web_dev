from flask import Flask, render_template, url_for, session, redirect
from forms import shift_form, conversion_form
from flask_session import Session
from database import get_db, close_db

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"

app.config("SESSION_PERMANENT") = False
app.config("SESSION_TYPE") = "filesystem"
Session(app)

app.teardown_appcontext(close_db)
    
@app.route("/guess", methods=["GET", "POST"])
def guess():
    form = shift_form()
    plaintext = form.plainText.data
    shift = form.shift.data

    cipherText = ""
    if form.validate_on_submit():

        for char in plaintext:
            if char.isupper():
                cipherText += chr((ord(char) - 65 + shift) % 26 + 65)
            elif char.islower():
                cipherText += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                cipherText += char
        form.cipherText.data = cipherText
        return render_template("shift_form.html", form=form )


        
    return render_template("shift_form.html", form=form)
x