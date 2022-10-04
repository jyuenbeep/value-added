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
It is in the path of the webpage.
2. This prints to the terminal --- " Serving Flask app 'app' "s.
3. This prints the name of the Flask app, which is by default the name of the file.
4. The return prints to the website because it is returning a value to the Flask function.
5. app.run() just runs the function. It is very similar to other languages, such as Python,
except Python doesn't use the word run.
...
INVESTIGATIVE APPROACH:
1. I downloaded Flask.
2. I ran the file.
3. I looked at the output and answered the questions.
4. I compared with my teammates to solidy by answers.
5. I gained a better understanding of Flask and revised by answers.
'''
