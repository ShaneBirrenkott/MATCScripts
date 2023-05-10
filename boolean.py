#!/usr/bin/env python3
#Boolean Logic basics
import time
import random

print("""You enter a dark room with two doors. 
Do you go through door #1, #2, or #3?""")
door = input("-> ")
if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?\n")
    print("1. Eat the cake.")
    print("2. Eat the bear.")
    bear = input("-> ")
    if bear == "1":
        print("1) The bear eats your face off. Good job!")
    elif bear == "2":
        print("2) The bear eats your legs off. Good job!")
    else:
        print(f"N)Well, doing {bear} is probably better.")
        print("Bear runs away.")
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.\n")
    print("1. Explain the physics of blueberries.")
    print("2. Tell him that technically speaking bananas are berries.")
    print("3. Understanding revolvers yelling melodies.")
    insanity = input("-> ")
    if insanity == "1" or insanity == "2":
        print("1) Cthulhu like berry math.")
        print("1) Good job!")
    else:
        print("N) The insanity rots your eyes into a pool of blueberry juice.")
        print("N) Good job!")

elif door == "3":
    print("A large man stands before you holding a baseball bat.\n")
    time.sleep(0.5)
    print("1. Say 'Son, let's play a nice wholesome ball game!'")
    time.sleep(0.5)
    print("2. Give him a cookie.")
    time.sleep(0.5)
    print("3. Write whatever you want and see what happens")
    time.sleep(0.5)
    baller = input("-> ")
    time.sleep(0.5)
    if baller == "1":
        print("With teats in his eyes, he hugs you and says 'Yes! I'd love that! There's just one thing...")
        time.sleep(0.5)
        print("'I'm the Daddy here.' You live out the rest of your life with muscley bat guy as your daddy.")
    elif baller == "2":
        print("He shouts 'I'm diabetic you sick frick!' and gives you diabeetus.")
    else:
        print(f"{baller}? A bold choice. Let's see how that works out for you.")
        roll = random.randrange(0,3)
        time.sleep(1)
        if roll == 0:
            print(f"Wow, '{baller}' was super lame. You die instantly from cringe.")
        elif roll == 1:
            print("Suddenly, aliens descend and pronounce you man and wife. You're married now.")
        else:
            print("The man approaches you and whispers his true name in your ear.")
            time.sleep(0.5)
            print("You become enlightened and live out your life as the God of your own universe.")
else:
    print("You did not select a door??? You have been cancelled by the activist group 'Stand Together Doors'.")
    time.sleep(0.5)
    print("You should have known better than to mess with STDs, you die from shame.")