from flask import Flask, render_template, request
from forms import shift_form, conversion_form

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
    
@app.route("/shift", methods=["GET", "POST"])
def shift():
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

    
@app.route("/conversion", methods=["GET", "POST"])
def conversion():
    form = conversion_form()
    return render_template("conversion_form.html", form=form)
