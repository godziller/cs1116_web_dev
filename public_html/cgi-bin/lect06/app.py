from flask import Flask, render_template, request
from forms import BMIForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
    
@app.route("/shift", methods=["GET", "POST"])
def bmi():
    form = BMIForm()
    if form.validate_on_submit():
    
    return render_template("shift_form.html", form=form)
