#!/usr/bin/env python3

#Shane Birrenkott, SBirrenkott@MadisonCollege.edu
#This script practices slicing and working with strings

varRed = "Red"
varGreen = "Green"
varBlue = "Blue"
varName = "Timmy"
varLoot = 10.4516295

#Print variable
print(f"Your {varGreen} Output")
print(f"Hello {varName}")
print(f"{varRed}-{varGreen}-{varBlue}")
print(f"Is this {varGreen.lower()} or {varBlue.lower()}?")
print(f"My name is {varName.upper()}")
print(f"[{varRed:+^7s}]")
print(f"[{varGreen.lower():=<7s}]")
print(f"[{varBlue.lower():*>9s}]")
print(f"{varBlue*10}")
print(f"{varLoot}")
print(f"{round(varLoot,1)}")
print(f"I have ${varLoot:.2f}")
print(f"[{varRed:$^10s}][{varGreen:$^9s}][{varBlue:$^10s}]")
print(f"[{varRed[::-1]: ^7s}][{varGreen: ^7s}][{varBlue[::-1]: ^7s}]")
print(f"First Color:[{varRed}] Second Color:[{varGreen}] Third Color:[{varBlue}]")