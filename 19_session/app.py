"""
Blue Haired Gals With Pronouns: Jasmine Yuen, Talia Hsia, Ziying Jian
SoftDev
K19 - Flask app that uses session capabilites to allow user to login and logout
2022-11-03
time spent: 
"""

from flask import Flask            
from flask import render_template   
from flask import request 
from flask import session

app = Flask(__name__)  



@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    if request.method == 'POST':
        if authenticate(request.form['username'],
                        request.form['password']):


@app.route("/login", methods=['GET', 'POST'])
def authenticate():
    

if __name__ == "__main__": 
    app.debug = True
    app.run()