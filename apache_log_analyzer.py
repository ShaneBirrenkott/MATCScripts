#!/usr/bin/env python3
#Shane Birrenkott, SBirrenkott@MadisonCollege.edu
#This script analyzes apache logs

import subprocess, argparse, json, requests
from urllib.request import urlopen

#Create a parser that will check for user input later
parser = argparse.ArgumentParser()

#This function runs the subprocess command to analyze the apache log
def IPAddressCount(apache_log_file_name):
    #Store my command in a string
    command = "cat "+apache_log_file_name+" | cut -d ' ' -f1 | sort -n | uniq -c | sort -n | tail -n5"
    #Execute that command and store it in a variable
    comCom = subprocess.run([command], shell=True, stdout=subprocess.PIPE)
    #Convert that variable to a string so it can be returned and printed
    comString = comCom.stdout.decode("utf-8")
    return comString

def main():
    #Introduce code and create my runScript boolean
    print("\nThis script analyzes apache logs.\n")
    runScript = False

    #List of acceptable inputs that continue the script
    yes = ["y","yes","yeah","sure","ok buddy", "c", "continue"]

    #Create the arguments that we will check for
    parser.add_argument('-c', '--continue', dest='varString', type=str, required=False, help="Run the script")
    args = parser.parse_args()

    #Check if there was an acceptable input for argparse to run the main script
    if args.varString in yes:
        runScript = True
        print(f"You chose {args.varString}, so we will continue")

    #IF not, manunally get input from the user to check if the script will run or not
    else:
        #This loop exists to give the user multiple attempts to provide the correct input
        while True:
            cont = input("\nWould you like to continue?: ").lower()
            if cont in yes:
                runScript = True
                break
            else:
                print(f"\nSorry, I don't understand '{cont}'\nPlease try again. Acceptable inputs are {yes}")

    #The main script if the user said yes to continue above, will not execute if they didn't
    if runScript == True:
        #Call my function to analyze the log
        comOutput = IPAddressCount("m5-access.log")
        #Create a new file to store the output from the original m5-access.log, without erasing the original apache_analysis.log
        comLog = open("new_apache_analysis.txt", 'w')
        #Clear the previous contents of the file so we're starting fresh, and ensure we start at the top
        comLog.truncate
        comLog.seek(0)
        #Write what the IPAddressCount function returned to a file
        comLog.write(comOutput)

        #       Milestone 10 Step 1: Break Down IP Address
        splitCom = comOutput.split("\n")
        #The list has a blank entry at the end that was causing problems, so this removes it
        splitCom.pop()
        #This variable will be used to help me iterate through the list in the for loop below
        count = len(splitCom)-1

        #This variable will be used to compare the counts of each IP and determine which has the highest count
        ipCount = 0

        #In this loop I strip the spaces from each line so our list is much cleaner, and find the IP with the biggest count
        for item in splitCom:
            #Remove spaces from the line
            splitCom[count] = splitCom[count].strip()

            #Seperate the count from the IP so I can compare counts
            compIP = splitCom[count].split(" ")
            #Check if the count in this line is bigger than the previous one, and save it if it is
            if int(compIP[0]) > ipCount:
                ipCount = int(compIP[0])

            #This helps us iterate through the list
            if count > 0:
                count -= 1
        
        #Technically redundant, but this second for loop ensures that we are only looking at the most frequest IP using the information parsed above
        for line in splitCom:
            #Find the like that had the highest count
            if str(ipCount) in line:
                #Seperate the IP from the return code in the most frequent IP address
                bigIP = line.split(" ")
                bigIP = bigIP[1]

                #Print the most frequent IP, and look up information about it
                print(bigIP)

                #Call the IPLookup Function to get info about our given IP address
                response = IPLookup(bigIP)

                #   Milestone 12 Step 4: Find information about the IP address
                response = json.loads(response)

                #print(response["data"]["attributes"]["last_analysis_stats"])
                bDef = response["data"]["attributes"]["last_analysis_results"]["BitDefender"]["category"]
                print(f"Bitdefender category: {bDef}")

                #Iterate through the dictionary and pull the organization and city
                # for pair in response.items():
                #     if pair[0] == "org":
                #         print(f"Organization: {pair[1]}")
                #     elif pair[0] == "city":
                #         print(f"City: {pair[1]}")
    else:
        #The script will quit if the user doesn't say yes to continue, this is here for troubleshooting just in case
        print(f"You chose {args.varString} so the script did not run")

#                   Milestone 12 Step 2: Call the Virus Total API
def IPLookup(IPaddress):

    #Get the API key from the file
    credFile = open('/home/student/credentials-vt', 'r')
    credentials = credFile.readlines()
    apiKey = credentials[0].split('=')[1].strip()

    #Store the url for virus total in a url that takes a custom IP
    url = f"https://virustotal.com/api/v3/ip_addresses/{IPaddress}"

    #Print that URL showing the IP used
    print(url)

    #               Milestone 12 Step 3: Add your API key to the call
    headerVariable = {'x-apikey':apiKey}
    response = requests.get(url, headers=headerVariable)

    #Turn the variable into one that will be easier to parse when passed back to the main function
    response = json.dumps(response.json())

    return response

#Main() function only runs if the code is called directly
if __name__=='__main__':
    main()