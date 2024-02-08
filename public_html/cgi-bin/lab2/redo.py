from flask import Flask, render_template, request

app = Flask(__name__)

# Morse Helper stuff
morse_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "" : "/"
}

def charToMorse(singleChar):
    try:
        return (morse_dict[singleChar])
    except KeyError:
        raise Exception('You have entered a character with no morse mapping')

def stringToMorse(alphaSoup):
    morse = ""
    alphaSoup = alphaSoup.strip().upper()
    
    for char in alphaSoup:
        print(char)
        print(type(char))
        morse = morse + charToMorse(char)
    print(morse)    
    return morse

# convert helper stuff
def check_input(i, c):
    
    # using xor here to catch 2 correct outa 4 pemutations
    if (i != '') ^ (c != ''):
        print("correct")
        return True
    else:
        raise Exception ("looks something funky, try again")
        print("malformed")
        return False

def convert_temp(i, c):
    
    #result = [inches, centimeters] in that order.
    result = []

    try:
        if c == '':
            print("c blank")
            result.append(float(i))
            centi = round(float(i) * 2.54, 2)
            print (centi)
            result.append(centi)
            print(result)
        else:
            print("i blank")
            inch = round(float(c) / 2.54, 2)
            result.append(inch)
            result.append(float(c))
            print(result)

        print(result)
        return result
    except:
        # Spotted the float conversion will throw execption - handy for non Z numbers
        raise Exception("Looks like you did not enter valid int or float??")

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
        try:
            message = request.form["message"]
            morse = stringToMorse(message)
            print(morse)
            return render_template("morse_response.html", message=morse)
        except Exception as error_message:
            print(error_message)
            return render_template("morse_form.html", error_message=error_message)
 
@app.route("/convert", methods=["GET","POST"])
def convert():
    if request.method == "GET":
        return render_template("convert_form.html",error_message="")
    else:
        try:
            inches = request.form["inches"]
            centimeters = request.form["cm"]
            check_input(inches, centimeters)
            
            result = convert_temp(inches, centimeters)
            print(result)
            return render_template("convert_form.html", cm=result[1], inches=result[0])

        except Exception as err:
            print(err)
            return render_template("convert_form.html", error_message=err)
