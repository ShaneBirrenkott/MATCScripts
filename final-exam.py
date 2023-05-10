#!/usr/bin/env python3
#Shane Birrenkott, SBirrenkott@MadisonCollege.edu

#I store my name in a variable because I'll need to reference it later, for now I print it here
name = "Shane Birrenkott"
print(f"Name: {name}")

#Import what I'll need to use later on
import subprocess, argparse, json, requests, bs4

def main():
    #The first part of the URL I'll be accessing later
    varServerName = "www.py.land"

    #Dictionary that will use argparse to determine which function to call based on the letter inpurred
    varMappingDict = {"A": "get_response", "B": "parse_string", "C": "parse_header", "D": "parse_json", "E": "get_cpu_usage"}

    #This variable will be used to store the dictionary value based on the user's input and check for empty argparse
    #Note - if statement checking if string was empty using False didn't work for whatever reason, so I did it this way
    inputKey = ""

    #Parser that argparse will use to parse args
    parser = argparse.ArgumentParser()

    #Add arguments to the parser, and set a variable to store the argument
    parser.add_argument('-f', '--functionKey', dest='arg', required=True, help="Input one of the following letters.\n\tA: get_response\n\tB: parse_string\n\tC: parse_header\n\tD: parse_json\n\tE: get_cpu_usage")
    args = parser.parse_args().arg

    #Loop throught the dictionary and see if they user inputted a valid key regardless of case
    for key in varMappingDict:
        if key == str(args).upper():
            #This print statement confirms which letter/function was called, but is commented so the output matches the requirement exactly
            #Uncomment for troubleshooting
            #print(f"You entered {key} which maps to {varMappingDict[key]}")

            #Store the key they picked in the variable we created earlier, this will be used to call the appropriate function
            inputKey = varMappingDict[key]

    #Check if no valid argument was found, and tell the user what the valid inputs are
    if inputKey == "":
        print("Invalid argument. Input one of the following letters.\n\tA: get_response\n\tB: parse_string\n\tC: parse_header\n\tD: parse_json\n\tE: get_cpu_usage")

        #Stop the script here, otherwise it will continue and print an empty URL which is unhelpful
        quit()

    #Assemble our final URL using the user input and our variable that stores the server name
    url = f"http://{varServerName}/{inputKey}"

    #Show the user what URL will be used
    print(f"URL is {url}")

    #Check which key (letter) the user entered and call the appropriate function
    if inputKey == varMappingDict["A"]:
        print(f"Answer:  {get_response(url)}")

    elif inputKey == varMappingDict["B"]:
        print(f"Answer:  {parse_string(url)}")

    elif inputKey == varMappingDict["C"]:
        print(f"Answer:  {parse_header(url)}")

    elif inputKey == varMappingDict["D"]:
        print(f"Answer:  {parse_json(url)}")

    elif inputKey == varMappingDict["E"]:
        print(f"Answer:  {get_cpu_usage(url)}")

#A
def get_response(url):
    #Get and return the text from that URL
    response = requests.get(url).text

    return response

#B
def parse_string(url):
    #Grap the H3 element from this URL
    response = str(bs4.BeautifulSoup(requests.get(url).text, "html.parser").find("h3"))

    #Slice the string to find the hidden message, append my name using the variable above, and return it
    response = f"{response[58:4:-5]} {name}"

    return response

#C
def parse_header(url):
    #Get and return the HTTP header with the corrisponding tag
    response = requests.get(url).headers['MATC_SPRING2023']

    return response

#D
def parse_json(url):
    #Get the json data from this url and store it in a dictionary
    response = json.loads(requests.get(url).text)

    #Parse the results to only get the entry for Ol' Dermy, and return the date and venue
    for entry in response['events']:
        if entry['artist'] == "Dermott Kennedy":
            response = f"On {entry['date']} at {entry['location']['name']}"

    return response

#E
def get_cpu_usage(url):
    #The command to be used
    command = "top -b -n1"

    #Run that command and convert it into a useable variable
    response = subprocess.run([command], shell=True, stdout=subprocess.PIPE).stdout.decode("utf-8")
    
    #Slice the result so that we only get the parts that we want
    response = response.split("\n")[2].split(" ")[1]

    #Format it to display in a readable way
    response = f"CPU Usage: {response}%"

    return response

#Execute main function only if the full script is called
if __name__ == "__main__":
    main()