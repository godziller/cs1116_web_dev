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

###############################################################################################################################################
  ####     #####
 #    #         #
 #    #    #####
 #   ##    #
  ### ##   ######
############################################################################################################################################3#


def situtationStation(Selected, Desired, baseValue):
    if Selected == 'Fahrenheit':
        if Desired == 'Celsius':
            ourPath = fahrenheitToCelsius(baseValue)
            return ourPath
        elif Desired == 'Kelvin':
            ourPath = fahrenheitToKelvin(baseValue)
            return ourPath
        else:
            ourPath = baseValue
            return ourPath

    elif Selected == 'Celsius':
        if Desired == 'Kelvin':
            ourPath = celsiusToKelvin(baseValue)
            return ourPath
        elif Desired == 'Fahrenheit':
            ourPath = celsiusToFahrenheit(baseValue)
            return ourPath
        else:
            ourPath = baseValue
            return ourPath

    elif Selected == 'Kelvin':
        if Desired == 'Fahrenheit':
            ourPath = kelvinToFahrenheit(baseValue)
            return ourPath
        elif Desired == 'Celsius':
            ourPath = kelvinToCelsius(baseValue)
            return ourPath
        else:
            ourPath = baseValue
            return ourPath

def celsiusToFahrenheit(Celsius):
    returningValue = Celsius * 1.8 + 32 
    return returningValue

def kelvinToFahrenheit(kelvin):
    returningValue = (kelvin-273) * 1.8 + 32 
    return returningValue

def fahrenheitToCelsius(fh):
    returningValue = (fh-32) * 0.55 
    return returningValue

def celsiusToKelvin(celsius):
    returningValue = celsius + 273
    return returningValue

def kelvinToCelsius(kelvin):
    returningValue = kelvin - 273
    return returningValue

def fahrenheitToKelvin(fh):
    returningValue = (fh-32) * 1.8 + 273
    print(returningValue)
    return returningValue


@app.route("/conversion", methods=["GET", "POST"])
def conversion():
    form = conversion_form()

    if form.validate_on_submit():
        selectedOption = form.base.data
        desiredOption = form.output.data
        outValue = 1234
        print(f'selected: {selectedOption}')
        result = situtationStation(selectedOption, desiredOption,form.baseValue.data)
        form.outValue.data = result

        return render_template("conversion_form.html", form=form)
    return render_template("conversion_form.html", form=form)