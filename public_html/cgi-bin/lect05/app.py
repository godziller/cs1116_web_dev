from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/morse", methods=["GET","POST"])
def morse():
    if request.method == "GET":
        return render_template("morse_form.html")
    else:
        message = request.form["message"]
        message = message.strip().upper()
        morse = ""
        #to do 
        morse_dict = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "" : "/"
        }
        for char in message:
            morse = morse + morse_dict[char] + ""
        morse  = " ".join([morse_dict[char]]) + " "
        return render_template("morse_response.html", message=message,morse=morse)
    
@app.route("/bmi", methods=["GET", "POST"])
def bmi():
    if request.method == "GET":
        return render_template("bmi_form.html",weight=weight, height=height,bmi=bmi, error="")
    else:
        weight = request.form["weight"]
        height = request.form["height"]
        if weight == "" or height == "":
            return render_template("bmi_form.html",weight=weight, height=height,bmi=bmi)
        weight = float(weight)
        height = float(height)
        bmi = weight / (height * height)
        return render_template("bmi_form.html",weight=weight, height=height,bmi=bmi, error="")