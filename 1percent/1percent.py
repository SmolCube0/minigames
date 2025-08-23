print("LOADING ASSETS...")
import random as r
import time as t
from decimal import *
# import keyboard as key #type: ignore

score = 1
percent = 1.01
increments = 0
coins = 0
answer = ""
achievements = {
    10:"Sub-atomic Gains",
    25:"Atomic Gains",
    50:"Forming a Molecule",
    100:"Thou Shalt Not Stop Improving",
    150:"DNA Discovery",
    200:"Single-Celled Organisms",
    250:"Cellular Mitosis",
    300:"Complex Organisms",
    365:"Atomic Habits"
}
achieveInc = [100,200,365,500,1000]

print("FINISHED.")
t.sleep(0.5)

print("Welcome to 1 Percent.")
print("This is a game where your score increases by 1% each time.")
print("Press the enter key to increment the score.")

while not False:
    answer = input("")
    if answer == "":
        score = round((score * percent),6)
        increments += 1
        print(f"Score: {score}")
        print(f"Percent: {round((percent-1)*100,3)}%")
        print(f"Times incremented: {increments}")
        t.sleep(0.05)
        if increments in achievements:
            print(f"Achievement Earned!\n{achievements[increments]}")
            if increments in achieveInc:
                percent += 0.01
                print(f"Your score now increases by {round((percent-1)*100,3)}% each increment. Keep up the good work!")

    if increments % 100 == 0:
        print("Type 'shop' to go to the shop, or press any other key to skip. \nWould you like to go to the shop?\n")
        t.sleep(1)
        answer = input("")
        if answer == 'shop':
            t.sleep(0.3)
            print("\nSHOP")
            print(f"The conversion rate from percent to coins is 1 to 2.")
            print("Converting percent removes it from your percentage increase, and you can no longer use it in-game.")
            answer = input("Type 'convert' to open the conversion menu or press enter to skip.\nWould you like to convert percentage?\n")
            if answer == 'convert':
                answer = percent
                while int(answer) <= round(percent):
                    answer = int(input(f"You have {round((percent-1)*100,3)} percentage points right now. Input the number of percentage points you would like to convert.\n"))
                    if answer < round((percent-1)*100,3):
                        break
                coins += answer
                percent -= answer
                print(f"You have {coins} coins and {round((percent-1)*100,3)} percentage points.")

