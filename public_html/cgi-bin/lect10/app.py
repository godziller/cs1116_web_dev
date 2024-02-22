from flask import Flask, render_template, make_response,request
from forms import VoteForm
from fask import FLask, session, redirect
from flask_session import Session

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"

@app.route("/vote", method=["GET", "POST"])
def vote():
    if request.cookies.get("voted") == "yes":
        return render_template("feedback.html", message = "Youve voted already")
        
    form = VoteForm()
    if form.validate_on_submit():
        vote = form.vote.data
        response  = make_response(render_template("feedback.html", message = "Thanks for your vote"))

        response.set_cookie("voted", "yes", max_age=5*365*24*60*60)
        return response
    return render_template("vote_form.html", form=form)