print("LOADING ASSETS...")
import pandas as pd
import random as rd
import time as t
import keyboard as kb
countries=['AFGHANISTAN', 'ANGOLA', 'ALBANIA', 'ANDORRA', 'UNITED ARAB EMIRATES', 'ARGENTINA', 'ARMENIA', 'ANTIGUA AND BARBUDA', 'AUSTRALIA', 'AUSTRIA', 'AZERBAIJAN', 'BURUNDI', 'BELGIUM', 'BENIN', 
      'BURKINA FASO', 'BANGLADESH', 'BULGARIA', 'BAHRAIN','BAHAMAS', 'BOSNIA AND HERZEGOVINA', 'BELARUS', 'BELIZE', 'BOLIVIA', 'BRAZIL', 'BARBADOS', 'BRUNEI', 'BHUTAN', 'BOTSWANA', 'CENTRAL AFRICAN REPUBLIC', 
      'CANADA', 'SWITZERLAND', 'CHILE', 'CHINA', "IVORY COAST", 'CAMEROON', 'DEMOCRATIC REPUBLIC OF THE CONGO', 'REPUBLIC OF CONGO', 'COOK ISLANDS', 'COLOMBIA', 'COMOROS', 'CAPE VERDE', 'COSTA RICA', 'CUBA', 
      'CYPRUS', 'CZECHIA', 'GERMANY', 'DJIBOUTI', 'DOMINICA', 'DENMARK', 'DOMINICAN REPUBLIC', 'ALGERIA', 'ECUADOR', 'EGYPT', 'ERITREA', 'WESTERN SAHARA', 'SPAIN', 'ESTONIA', 'ETHIOPIA', 'FINLAND', 'FIJI', 
      'FRANCE', 'MICRONESIA', 'GABON', 'UNITED KINGDOM', 'GEORGIA', 'GHANA', 'GUINEA', 'GAMBIA', 'GUINEA BASSAU', 'EQUATORIAL GUINEA', 'GREECE', 'GRENADA', 'GUATEMALA', 'GUYANA', 'HONG KONG', 'HONDURAS', 
      'CROATIA', 'HAITI', 'HUNGARY', 'INDONESIA', 'INDIA', 'IRELAND', 'IRAN', 'IRAQ', 'ICELAND', 'ISRAEL', 'ITALY', 'JAMAICA', 'JORDAN', 'JAPAN', 'KAZAKHSTAN', 'KENYA', 'KYRGYZSTAN', 'CAMBODIA', 'KIRIBATI',
      'SAINT KITTS AND NEVIS', 'SOUTH KOREA', 'KUWAIT', "LAOS", 'LEBANON', 'LIBERIA', 'LIBYA', 'SAINT LUCIA', 'LIECHTENSTEIN', 'SRI LANKA', 'LESOTHO', 'LITHUANIA', 'LUXEMBOURG', 'LATVIA', 'MACAO', 'MOROCCO', 'MONACO', 
      'MOLDOVA', 'MADAGASCAR', 'MALDIVES', 'MEXICO', 'MARSHALL ISLANDS', 'NORTH MACEDONIA', 'MALI', 'MALTA', 'MYANMAR', 'MONTENEGRO', 'MONGOLIA', 'MOZAMBIQUE', 'MAURITANIA', 'MAURITIUS', 'MALAWI', 'MALAYSIA', 
      'NAMIBIA', 'NIGER', 'NIGERIA', 'NICARAGUA', 'NIUE', 'NETHERLANDS', 'NORWAY', 'NEPAL', 'NAURU', 'NEW ZEALAND', 'OMAN', 'PAKISTAN', 'PANAMA', 'PERU', 'PHILLIPINES', 'PALAU', 'PAPUA NEW GUINEA', 'POLAND', 'NORTH KOREA', 
      'PORTUGAL', 'PARAGUAY', 'PALESTINE', 'QATAR', 'ROMANIA', 'RUSSIA', 'RWANDA', 'SAUDI ARABIA', 'SUDAN', 'SENEGAL', 'SINGAPORE', 'SOLOMON ISLANDS', 'SIERRA LEONE', 'EL SALVADOR', 'SAN MARINO', 'SOMALIA', 
      'SERBIA', 'SOUTH SUDAN', 'SAO TOME AND PRINCIPE', 'SURINAME', 'SLOVAKIA', 'SLOVENIA', 'SWEDEN', 'ESWATINI', 'SEYCHELLES', 'SYRIA', 'CHAD', 'TOGO', 'THAILAND', 'TAJIKISTAN', 'TURKMENISTAN',
      'EAST TIMOR', 'TONGA', 'TRINIDAD AND TOBAGO', 'TUNISIA', 'TURKIYE', 'TUVALU', 'TAIWAN', 'TANZANIA', 'UGANDA', 'UKRAINE', 'URUGRAY', 'UNITED STATES', 'UZBEKISTAN', 'VATICAN CITY', 'SAINT VINCENT AND THE GRENADINES', 
      'VENEZUELA', 'VIETNAM', 'VANUATU', 'SAMOA', 'YEMEN', 'SOUTH AFRICA', 'ZAMBIA', 'ZIMBABWE','KOSOVO']

invalidGuess = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
def infoPage():
    print("Your score is 10 minus the number of attempts you took to guess the country.")
    print("If you failed to guess the country, you get 0 points.")
    print("All countries with 'Saint' are spelled 'saint'.")
    print("All countries with 'Island(s)' are spelled 'Island(s), depending on if they have multiple.")
    print("All countries have had their names changed to more familiar names.")
    print("eg. Democratic People's Republic of Korea -> North Korea.")
    print("Partially recognized countries, like Palestine, Kosovo, and West Sahara, are included.")
    print("Press enter to continue to the game.")
    while True:
        if kb.is_pressed('enter'):
            if kb.is_pressed('enter'):
                print("Let's go!")
                break

def hangmanGame():
    lives = 6
    letters = ""
    display = ""
    guess = ""
    country = countries[rd.randint(0,len(countries))]
    spaces = country.count(' ')
    nameList = country.split()
    nameLengths = [len(name) for name in nameList]

    if spaces==0:
        print("There is 1 word in this country's name.")
    else:
        print(f"There are {spaces+1} words in this country's name.")

    for i in range(0,len(nameList)):
        for j in range(0,nameLengths[i]):
            if j==nameLengths[i]:
                display = display + '_'
            else:
                display = display + '_ '
        if spaces==0:
            print(f"There are {nameLengths[i]} letters in this country's name.")
        elif j==nameLengths[i]:
            print(f"There are {nameLengths[i]} letters in word {i} of this country's name.")
        else:
            display = display + '/ '
            print(f"There are {nameLengths[i]} letters in word {i} of this country's name.")
        
    print(display)
    t.sleep(1)
    guess = input("")
    guess = input(" ")
    while True:
        if guess == "":
            guess = input("Start guessing. Guess one capital letter or the whole name.")
        if guess in country:
            print(f"Nice guess!")
            display = ''.join([guess if c == guess else '/ ' if c == ' ' else '_ ' for c in country])
            print(f"Your word is {display}, and you have {livesdict[lives]} drawn right now.")
            print(f"Your incorrect letters are {letters}.")
            guess = ""
            continue
        elif guess == country:
            guess = ""
            break
        elif guess in invalidGuess:
            guess=guess.swapcase()
            continue
        else:
            lives -= 1
            letters += guess
            print(f"Oof, that's wrong. You have {livesdict[lives]} drawn right now.")
            print(f"Your incorrect letters are {letters}. ")
            guess = ""
            continue


    global score
    score += (10-lives)
    print(f"Congratulations! You guessed the correct answer! You earned {score} points!")
print("STARTING GAME...")

# startup

score = 0
rounds = 0
playAgain = True
livesdict = {
    6: "nothing",
    5: "the head",
    4: "the head & body",
    3: "the head, body, & left arm",
    2: "the head, body, & both arms",
    1: "the head, body, both arms, & right leg",
    0: "full"
}

print("Hi, today we're going to play Hangman using the names of countries as words.")
print("At the beginning, I will think of a country and tell you how many words and letters there are.")
print("Then, you will get 6 chances to guess the country. The chances are the the head, body, arms, and legs.")
print("Make sure all answers are capital letters, eg. CANADA.")
print("No special characters needed.")
print("Ready? Press enter to start, or press 0 for info.")
while True:
    if kb.is_pressed('enter'):
        print("Let's go!")
        t.sleep(1)
        break
    elif kb.is_pressed('0'):
        infoPage()
        break

# game
while playAgain == True:
    rounds += 1
    t.sleep(1)
    hangmanGame()
    playAgain = input("Do you want to play again? (Y/N/menu)")
    if playAgain == "Y" or playAgain == "y":
        print("Great! Get ready...")
        continue
    elif playAgain == "info":
        print("Taking you to info...")
        t.sleep(0.5)
        infoPage()
        continue
    else:
        print(f"Oh. At least your final score was {score} through {rounds} rounds of playing.")
        print(f"You earned an average of {score/rounds} points per round. Anyways. Bye.")
        break