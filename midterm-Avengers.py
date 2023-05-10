#!/usr/bin/env python3
print("Name: Shane Birrenkott")

#This script compares user inputs to keys and values in a dictionary

#Create our dictionaries
avenger_database = {"Hero":"Ironman", "Superpower":"Suit"}
action_database = {"Punch":"Ok. That will only tickle Thanos.", "Blast":"OK. That will slow down Thanos.", "Sacrifice":"That is what it takes, we thank you."}

#Create our variables that count, and break our loop
infinity_stone_object = 0
counter = 0

#Initialize our loop and check if the counters are at their required values
while True:
    if infinity_stone_object == 0 or counter < 3:

        #Authenticate the user by seeing if they know these values
        input_hero = input("Hero: ")
        input_superpower = input("Superpower: ")

        if input_hero in avenger_database.values() and input_superpower in avenger_database.values():
            infinity_stone_object = 1
            print("Tony, you know what you need to do!")
            action = input(f"Please choose an action {action_database.keys()}: ")

            if action == "Punch":
                print(action_database["Punch"])

            elif action == "Blast":
                print(action_database["Blast"])

            elif action == "Sacrifice":
                print(action_database["Sacrifice"])
                break

            else:
                print("Maybe we should work with Thor")
        
        else:
            counter += 1
            if counter == 3:
                print("Call in Dr. Strange to find another option\n"*25)
                break

            else:
                print(f"You are not the hero I'm looking for {counter}")

    else:
        if counter == 3:
            print("Call in Dr. Strange to find another option\n"*25)
            break

        else:
            print(f"You are not the hero I'm looking for {counter}")
