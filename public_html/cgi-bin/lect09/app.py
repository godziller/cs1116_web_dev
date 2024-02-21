from flask import Flask, render_template, request
from database import get_db, close_db
from forms import WombatForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
    

        #gigs = db.execute("SELECT * FROM gigs; """).fetchall()

#in squal "yada yada = '%s' " % band
        # suseptible to SQL injection attacks
        #so protect yourself with this
#in sql "yada yada = ?;" (band,)
#fetchall returns a list whilst fetchone returns one dictionary type 

# next routes are to insert data

#note you dont have to fetch anything when you are writing to the sql (inserting)

#db.commit()
"""
i
"""