import random as r
import time as t
from decimal import *
import keyboard as key #type: ignore

def reactionTime(tutorial,KB):
    start = 0
    end = 0
    elapsed = 0

    if tutorial == True:
        print("This is a reaction time tester. When you see the word 'GO!', press enter.")
        print("The score you get is your reaction time rounded to the nearest tenth of a millisecond.")
        KBQ=input("Do you want to change the keybind? (default is 'enter')(Y/N)")
        if KBQ == "Y" or KBQ == "y":
            KB = input("Enter the keybind you want to use (default is 'enter'). To enter a letter or number, type that number. To enter spacebar, type space.")
        else:
            KB = 'enter'
        print("Get ready...")
    else: 
        print("Get ready...")
    t.sleep(r.randint(2,5))

    print("GO!!")
    start = t.perf_counter()
    while True:
        if key.is_pressed(KB):
            end = t.perf_counter()
            break
    t.sleep(0.5)
    elapsed = ((end - start) * 1000)
    RoundedScore = round(elapsed,3)
    return RoundedScore

def settingsMenu():
    keybind = input("Enter the keybind you want to use (default is 'enter'). To enter a letter or number, type that number. To enter spacebar, type space.")
    print("Returning to game.")
    t.sleep(1)
    return keybind

# startup
scores = []
fastestScore = 0
avgScore = 0
keybind = 'enter'
getcontext().rounding = ROUND_HALF_EVEN
currentScore = reactionTime(True,keybind) # game part
print(currentScore)

# results
fastestScore = currentScore
scores.append(currentScore)
avgScore = currentScore
print("Your reaction time is ",currentScore,"ms")
print("Your fastest time is ",fastestScore,"ms")
print("Your average reaction time is ",avgScore,"ms")

# looping part if continue
t.sleep(1)
dummy = input()
continuePlay = input("Do you want to continue? (Y/N/menu)")
if continuePlay=="Y" or continuePlay=="y":
    print("Nice, let's keep playing!")
    t.sleep(1)
elif continuePlay=="menu":
    print("Going to settings")
    t.sleep(0.5)
    keybind = settingsMenu()
    continuePlay="y"
else:
    print("Oh. Bye.")
    exit()

while continuePlay == "Y" or continuePlay == "y":
    currentScore = reactionTime(False,keybind)
    print("Your reaction time is ",currentScore,"ms")
    fastestScore = currentScore if currentScore < fastestScore else fastestScore
    scores.append(currentScore)
    avgScore = round((sum(scores)/len(scores)),3)
    print("Your fastest time is ",fastestScore,"ms")
    print("Your average reaction time is ",avgScore,"ms")

    dummy = input()
    continuePlay = input("Do you want to continue? (Y/N/menu)")
    if continuePlay=="Y" or continuePlay=="y":
        print("Nice, let's keep playing!")
        t.sleep(1)
    elif continuePlay=="menu":
        print("Going to settings")
        settingsMenu()
        continuePlay = "y"
        t.sleep(0.5)
    else:
        print("Oh. Bye.")
        exit()