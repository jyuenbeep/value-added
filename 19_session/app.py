"""
Blue Haired Gals With Pronouns: Jasmine Yuen, Talia Hsia, Ziying Jian
SoftDev
K19 - Flask app that uses session capabilites to allow user to login and logout
2022-11-03
time spent:
"""

from flask import request, Flask, render_template, redirect
from flask import session

app = Flask(__name__)

username = "ziying"
password = "john"

#app.secret_key = '74f9cf8fcf367b3c88469c1e720934b2298c4108928e85d4f79703f763942bf3'

def authenticate(user, passw):
    return (user == username and passw == password)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("login.html", errorLogin = "")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if authenticate(request.args['username'], request.args['password']):
        return render_template('response.html', functional="WORKS!")
    else:
        return render_template('login.html', errorLogin = "Bad password or bad username.")

if __name__ == "__main__":
    app.debug = True
    app.run()
