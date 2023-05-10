#!/usr/bin/env python3
#Shane Birrenkott, SBirrenkott@MadisonCollege.edu

import requests

response = requests.get('http://google.com')
print(response.text[:250:])

with open("google_backup.html", "w") as webFile:
    webFile.write(response.text)