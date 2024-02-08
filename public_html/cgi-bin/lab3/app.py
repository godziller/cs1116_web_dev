from flask import Flask

app = Flask(__name__)

@app.route("/rsp/<player>")
def rsp(player):
    return "Under Development!!!!!!!!!!!!!!!!!!!!!!"