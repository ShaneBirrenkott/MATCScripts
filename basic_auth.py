#!/usr/bin/env python3

import requests, json

credFile = open('/home/student/credentials', 'r')

credentials = credFile.readlines()
#username = credentials[0].split('=')[1].strip()
#password = credentials[1].split('=')[1].strip()

apiKey = credentials[2].split('=')[1].strip()

#url = "https://api.github.com/user"
#response = requests.get(url, auth=(username, password))

url = f"https://api.nytimes.com/svc/movies/v2/reviews/search.json"
parameters = {"api-key":apiKey,"query":"martian"}
headers = {blah blah}

response = requests.get(url, parameters, headers=header)

print(json.dumps(response.json(), indent=4))

#print(json.dumps(response.json(), indent=4))