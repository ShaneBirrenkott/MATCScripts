#!/usr/bin/env python3
print("Name: Shane Birrenkott")

#This script searches for keywords in a file and adds the line number to the total if one is found

#Open the file and make sure we're starting at the top
file1 = open("Midterm-if.txt")
file1.seek(0)

#Create the variable that will add up the matching lines
total = 0

#Loop through the file
for line in file1:
    #The file contains comma seperated values, so split each line on commas and store the resulting list
    searchTerm = line.split(",")

    #Check if the keyword matches our criteria, and incriment the total if it does
    if "ckneale8@weibo.com" in searchTerm:
        total += int(searchTerm[0])

    elif "247.224.231.109\n" in searchTerm:
        total += int(searchTerm[0])

    elif "Litchfield" in searchTerm:
        total += int(searchTerm[0])

    elif "205.36.91.89\n" in searchTerm:
        total += int(searchTerm[0])

    elif "Cassy" in searchTerm:
        total += int(searchTerm[0])

    elif "askeelqc@clickbank.net" in searchTerm:
        total += int(searchTerm[0])

#Print the total and close the file
print(f"The total is: {total}")
file1.close()