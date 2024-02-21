from flask import Flask, render_template, make_response,request
from forms import VoteForm
from 

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.teardown_appcontext(close_db)

@app.route("/vote", method=["GET", "POST"])
def vote():
    wines = db.execute("SELECT * from wines")
    form = VoteForm()
    
