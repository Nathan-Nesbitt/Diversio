"""
This program gets the current latitude/longitude of ISS
The purpose of this task is to point out issues with the program below if any
and improve it wherever applicable.

Comments Nathan Nesbitt:

This code seems pretty good. There were issues with the lettering, as they would
always default to S and W. To fix it I moved them before the `if float() > 0` 
lines which solves the problem. 

I also removed the use of r.status_code on `if int() == 200:` and 
`print("Request was unsuccessful: {}".format(st))` as it was already defined as
the variable `st`. 

I also fixed the variable `LonDir` to be camelcase `lonDir` to match the rest 
of the variables.

"""

import re
import requests
import time
from time import strftime
from time import localtime
import json

r = requests.get("http://api.open-notify.org/iss-now.json")
d = json.loads(r.text)
st = r.status_code

if int(st) == 200:
    ts = d["timestamp"]
    time = strftime("%T", localtime(ts))

    latitude = d["iss_position"]["latitude"]
    latDir = "S"
    if float(latitude) > 0:
        latDir = "N"

    longitude = d["iss_position"]["longitude"]
    lonDir = "W"
    if float(longitude) > 0:
        lonDir = "E"

    print("Current position of International Space Station at {}".format(time))
    print("Latitude: {}° {}".format(latitude, latDir))
    print("Longitude: {}° {}".format(longitude, lonDir))
else:
    print("Request was unsuccessful: {}".format(st))
