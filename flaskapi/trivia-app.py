#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)
## This is where we want to redirect users to
@app.route("/correct")
def correct():
    return "You got the right answer!"
@app.route("/") # user can land at "/"
def start():
    return render_template("trivia-app.html") # look for templates/postmaker.html
@app.route("/question", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        if request.form.get("answer"): # if nm was assigned via the POST
            answer = request.form.get("answer") # grab the value of nm from the POST
        else: # if a user sent a post without nm then assign value defaultuser
            answer = "No answer"
    elif request.method == "GET":
        if request.args.get("answer"): # if nm was assigned as a parameter=value
            answer = request.args.get("answer") # pull nm from localhost:5060/login?nm=larry
        else: # if nm was not passed...
            answer = "No answer" # ...then user is just defaultuser
    if answer == "Clark Kent":
        return redirect(url_for("correct")) # pass back to /success with val for name
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

