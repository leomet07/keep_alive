import os
import json
import requests
from time import sleep
from datetime import datetime


def get_data(filename):
    with open(filename, "r") as f:
        return json.load(f)


time = 1
# time = 60 * 5
while True:
    lines = get_data("urls.json")

    for line in lines:
        r = requests.get(line["url"])

        time_now = datetime.now()
        if (time_now.hour > 9 and time_now.hour < 22) or  ("night" in line and line["night"] == True):
          
            print("Run at night")

            time_now_str = str(time_now)[11:19]

            print(str(time_now_str) + " " + str(r.text))
        else:
            continue

    sleep(time)

