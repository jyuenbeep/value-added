"""
Jasmine Yuen
SoftDev
K07 -- Given this python file using Flask, try to learn how the code works.
time spent: 0.5

DISCO: Learned Flask is a viable tool to open websites with.
QCC: NONE
"""
from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
QCC:
0. Python.
1. It's in the link. It shows the number of the local host that serves your webpage.
2. This prints to the terminal --- " Serving Flask app 'app' ".
3. This prints the name of the Flask app, which is by default the name of the file.
4.  
5.
...
INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''
