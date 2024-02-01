from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/spy", methods=["GET","POST"])
def spy():
    if request.method == "GET":
        return render_template("names_form.html")
    else:
        firstName = request.form["firstName"].capitalize()
        secondName = request.form["secondName"].capitalize()
        return render_template("names_response.html", firstName=firstName, secondName=secondName)

   
@app.route("/morse", methods=["GET","POST"])
def morse():
    if request.method == "GET":
        error_message = ""

        return render_template("morse_form.html",error_message="")
    else:
        while True:
            try:
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
                print(morse)
                return render_template("morse_response.html", message=morse)
            except:
                print("error here")
                error_message = "please enter something proper into the box :/"
                return render_template("morse_form.html", error_message=error_message)
            else:
                break

@app.route("/morse", methods=["GET","POST"])
def morse():
    if request.method == "GET":
        error_message = ""

        return render_template("morse_form.html",error_message="")
                
