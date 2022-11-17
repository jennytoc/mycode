#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask import render_template

import json

app = Flask(__name__)

characterdata = [{
    "name" : "Jenni Tempest",
    "job" : "Black Mage",
    "type" : "DPS",
    "skills" : [
        "Blizzard",
        "Meteor Shower",
        "Thundara"
        ]
    }]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        data = request.json
        if data:
            data=json.loads(data)
            name = data["name"]
            job = data["job"]
            jobType = data["type"]
            skills = data["skills"]
            characterdata.append({"name": name, "job": job, "type": jobType, "skills": skills})
    return jsonify(characterdata)

@app.route("/character")
def printChar():
    return render_template("mini-project03.html", character = characterdata)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
