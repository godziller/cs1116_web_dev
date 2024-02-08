from flask import Flask, render_template, request
from forms import WombatForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
    
@app.route("/wombat", methods=["GET", "POST"])
def wombat():
    form = WombatForm()
    outcome = ''
    if form.validate_on_submit():
        wombat = form.wombat.data
        if wombat == True:
            outcome = "You're Wrong"
        else: 
            outcome = "You're Right"
        
        
    return render_template("wombatForm.html", form=form, title="Wombat Preferences", outcome=outcome)
