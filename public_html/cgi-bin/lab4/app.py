from flask import Flask, render_template
from database import get_db, close_db
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
        db = get_db()
        result = db.execute("""SELECT COUNT (*) FROM winners WHERE country = ?; """, (country,)).fetchone()[0]

        if result >0:
            countries = db.execute("""SELECT * FROM winners WHERE country = ?; """, (country,)).fetchall()
        else:
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
        db = get_db()

        countryResult = db.execute("""SELECT COUNT (*) FROM winners WHERE country = ?; """, (country,)).fetchone()[0]
        pointsResult = db.execute("""SELECT COUNT (*) FROM winners WHERE points >= ?; """, (points,)).fetchone()[0]
   
        print("Country result:", countryResult)
        print("Points result:", pointsResult)

        if countryResult > 0 and pointsResult > 0:
            # Both country and points are provided
            print('the big ones')
            countries = db.execute("""SELECT performer FROM winners WHERE country = ? AND points >= ?""", (country, points)).fetchall()
        elif countryResult > 0:
            countries = db.execute("""SELECT performer FROM winners WHERE country = ?; """, (country,)).fetchall()

        elif pointsResult > 0:
            points = int(points)
            print('getting points')
            pts = db.execute("""SELECT performer FROM winners WHERE points >= ?; """, (points,)).fetchall()  

        else:
            print('nope')
            countries = db.execute("""SELECT performer FROM winners """, ).fetchall()
        

    return render_template('minWinnerForm.html',caption='winners', form=form, countries=countries, points=pts)
