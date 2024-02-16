from flask import Flask, render_template
from database import EurovisionDB, get_db, close_db
from forms import winnerForm, minWinner
from datetime import datetime
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.teardown_appcontext(close_db)
    

@app.route("/winners", methods=["GET", "POST"])
def winners():
    form = winnerForm()
    countries = None
    error = 'This Country was not found in our database, please try again with a different country or check you spelling!'
   # return render_template('winnerForm.html', form=form)
    if form.validate_on_submit(): 
        country = form.country.data
        
        eurovision = EurovisionDB('app.db')
        countries = eurovision.getSingersList(country)

        if not countries:
            return render_template('winnerForm.html',caption='Eurovision winners', form=form, countries=countries, error=error)

    return render_template('winnerForm.html',caption='Eurovision winners', form=form, countries=countries)

@app.route("/min_winners", methods=["GET", "POST"])
def mineWinners():
    form = minWinner()
    countries = None
    pts = None

    if form.validate_on_submit(): 
        country = form.country.data
        points = form.points.data

        eurovision = EurovisionDB('app.db')

        print(country != "")
        print(points !="")

        if country and points:
            countries = eurovision.filterOnCountryAndPoints(country, points)
        elif country:
            countries = eurovision.getSingersList(country)
        elif points:
            pts = eurovision.getCountiesAbovePoints(points)
            print(pts)
        else:
            countries = eurovision.getAllWinners()  

    return render_template('minWinnerForm.html',caption='winners', form=form, countries=countries, points=pts)
