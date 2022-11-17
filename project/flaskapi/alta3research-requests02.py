#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL = "http://127.0.0.1:2224/"
new_character = {
    "name": "Alcain",
    "job" : "White Mage",
    "type" : "Healer",
    "skills" : [
        "Cura",
        "Raise",
        "Holy"
        ]}
new_character = json.dumps(new_character)
resp = requests.post(URL, json=new_character)
pprint(resp.json())
