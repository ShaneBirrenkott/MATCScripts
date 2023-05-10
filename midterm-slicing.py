#!/usr/bin/env python3
print("Name: Shane Birrenkott")

#This script slices a file into a new sentence

#Open our file and ensure we're starting from the top
file1 = open("slicing-file.txt")
file1.seek(0)

#Read the file into a string and split it by newline
readFile = file1.read()
readFile = readFile.split("\n")

a = readFile[-1]

b = " ".join(readFile[3:6])

c = " ".join(readFile[-8:-13:-2])

d = " ".join(readFile[12:16])

e = " ".join(readFile[-19:-21:-1])

quote = a+" "+b+" "+c+" "+d+" "+e

print(quote)

#Close our file
file1.close()