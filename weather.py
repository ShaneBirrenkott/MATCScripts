#!/usr/bin/env python3
#Shane Birrenkott, SBirrenkott@MadisonCollege.edu

import json
from urllib.request import urlopen

data = urlopen("https://goweather.herokuapp.com/weather/Madison")

data = json.loads(data.read())

for key, item in data.items():
    if key == "forecast":
        for entry in item:
            for key2, item2 in entry.items():
                    if key2 == "day":
                        print(key2, item2)
                    elif key2 == "temperature":
                        print(key, item2)


#   