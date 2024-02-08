from flask import Flask, render_template, request
from forms import BMIForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
    
@app.route("/bmi", methods=["GET", "POST"])
def bmi():
    form = BMIForm()
    if form.validate_on_submit():
        weight = form.weight.data
        height = form.height.data
        bmi = weight / (height * height)
        form.bmi.data = bmi
    return render_template("bmi_form.html", form=form)
