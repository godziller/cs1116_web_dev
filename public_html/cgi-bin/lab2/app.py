from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/spy", methods=["GET","POST"])
def spy():
    if request.method == "GET":
        return render_template("names_form.html")