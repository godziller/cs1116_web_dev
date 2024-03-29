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

@app.route("/convert", methods=["GET","POST"])
def convert():
    if request.method == "GET":
        return render_template("convert_form.html",error_message="")
    else:
        while True:
            try:
                inches = request.form["inches"]
                centimeters = request.form["cm"]
                blank = ''

                #to do 
                if centimeters != blank and inches == blank:
                    print("testing cm")
                    centimeters = float(centimeters)
                    lastInputInches = round(centimeters / 2.54, 2)
                    return render_template("convert_form.html", cm=centimeters, inches=lastInputInches  )
                
                elif inches != blank and centimeters == blank:
                    print("testing inches")
                    inches = float(inches)
                    lastInputCm = round(inches * 2.54, 2)
                    return render_template("convert_form.html", cm=lastInputCm, inches=inches)
                 
                    
                elif centimeters == blank and inches == blank:
                    error_message = "please enter something into ONE of your boxes:/"
                    raise ValueError("nothing entered")
                elif centimeters != blank and inches != blank:
                    error_message = "please empty one of your boxes in future:/"
                    raise ValueError("boxes full")

            except:
                print("error here")
                error_message = "please enter a value into ONE of the boxes in future :/"
                return render_template("convert_form.html", error_message=error_message)
            else:
                break

