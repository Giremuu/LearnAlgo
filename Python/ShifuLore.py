#
#   "Shifulore" is a Japanese-themed twist on the game Rock-Paper-Scissors. It made after Chapter 1, 2, 3 and 4 of "Legends of Python - Beginner" from Codédex + the sleep's module + \n for a better view in the terminal
#

import random
from time import sleep


print("\n\n[RULES] ShifuLore is a small 'Rock-Paper-Scissors' game with Japanese theme \n\nSamouraï > Oni \nOni > Kitsune\nKitsune > Samouraï \n\nEnter your pseudo and the number of round !")
print()
sleep(4)

name = input("Pseudo : ")
sleep(1)
bo = input("Do you want 3 rounds, 5 rounds or 7 rounds ? ")
scorePlayer = 0
scoreVanika = 0


#bo is in string and not in int to manage all user's entries without ErrorType
while bo != "3" and bo != "5" and bo != "7":
    bo = input("Not valid, you need to choose between 3, 5 or 7 : ")

if bo == "3":
    for i in range(0, 3, 1):
        print(f'\n\n Manche {i+1} : {name} vs Vanika \n')

        #Players think about their hand
        sleep(2)
        vanikaPlays = random.randint(1,3)           #1 = Samourai, 2 = Oni, 3 = Kitsune
        choose = input("What did you play ? Samourai, Oni or Kitsune ! ")
        print("Vanika choose her hand. . .")
        sleep(2)

        #Verification for user's entry :
        while choose != "Samourai" and choose != "Oni" and choose != "Kitsune":
            choose = input("Not valid, you need to choose between Samourai, Oni or Kitsune : ")
            sleep(3)

        #Compare user's hand against Vanika's hand
        if vanikaPlays == 1 and choose == "Oni":
            scoreVanika = scoreVanika + 1
            print(f"Vanika' Samourai slash {name}'s Oni !\nScore : {scorePlayer}/{scoreVanika}")

        elif vanikaPlays == 1 and choose == "Kitsune":
            scorePlayer = scorePlayer + 1
            print(f"{name}'s Kitsune crush {name}' Samourai !\nScore : {scorePlayer}/{scoreVanika}")

        elif vanikaPlays == 2 and choose == "Samourai":
            scorePlayer = scorePlayer + 1
            print(f"{name}' Samourai slash Vanika's Oni !\nScore : {scorePlayer}/{scoreVanika}")

        elif vanikaPlays == 2 and choose == "Kitsune":
            scoreVanika = scoreVanika + 1
            print(f"Vanika's Oni destroy {name}'s Kitsune !\nScore : {scorePlayer}/{scoreVanika}")

        elif vanikaPlays == 3 and choose == "Oni":
            scorePlayer = scorePlayer + 1
            print(f"{name}'s Oni destroy Vanika's Kitsune !\nScore : {scorePlayer}/{scoreVanika}")

        elif vanikaPlays == 3 and choose == "Samourai":
            scoreVanika = scoreVanika + 1
            print(f"Vanika's Kitsune crush {name}'s Samourai !\nScore : {scorePlayer}/{scoreVanika}")
        else:
            print("It's a draw.. \n")
    

#Copy Paste from the 3 rounds part
if bo == "5":
    for i in range(0, 5, 1):
        print(f'\n Manche {i+1} : {name} vs Vanika \n')

        #Players think about their hand
        sleep(2)
        vanikaPlays = random.randint(1,3)           #1 = Samourai, 2 = Oni, 3 = Kitsune
        choose = input("What did you play ? Samourai, Oni or Kitsune ! ")
        print("Vanika choose her hand. . .")
        sleep(2)

        #Verification for user's entry :
        while choose != "Samourai" and choose != "Oni" and choose != "Kitsune":
            choose = input("Not valid, you need to choose between Samourai, Oni or Kitsune : ")
            sleep(3)

        #Compare user's hand against Vanika's hand
        if vanikaPlays == 1 and choose == "Oni":
            scoreVanika = scoreVanika + 1
            print(f"Vanika' Samourai slash {name}'s Oni !\nScore : {scorePlayer}/{scoreVanika}")

        elif vanikaPlays == 1 and choose == "Kitsune":
            scorePlayer = scorePlayer + 1
            print(f"{name}'s Kitsune crush {name}' Samourai !\nScore : {scorePlayer}/{scoreVanika}")

        elif vanikaPlays == 2 and choose == "Samourai":
            scorePlayer = scorePlayer + 1
            print(f"{name}' Samourai slash Vanika's Oni !\nScore : {scorePlayer}/{scoreVanika}")

        elif vanikaPlays == 2 and choose == "Kitsune":
            scoreVanika = scoreVanika + 1
            print(f"Vanika's Oni destroy {name}'s Kitsune !\nScore : {scorePlayer}/{scoreVanika}")

        elif vanikaPlays == 3 and choose == "Oni":
            scorePlayer = scorePlayer + 1
            print(f"{name}'s Oni destroy Vanika's Kitsune !\nScore : {scorePlayer}/{scoreVanika}")

        elif vanikaPlays == 3 and choose == "Samourai":
            scoreVanika = scoreVanika + 1
            print(f"Vanika's Kitsune crush {name}'s Samourai !\nScore : {scorePlayer}/{scoreVanika}")
        else:
            print("It's a draw.. \n")


#Copy Paste from the 3 rounds part
if bo == "7":
    for i in range(0, 3, 1):
        print(f'\n Manche {i+1} : {name} vs Vanika \n')

        #Players think about their hand
        sleep(2)
        vanikaPlays = random.randint(1,3)           #1 = Samourai, 2 = Oni, 3 = Kitsune
        choose = input("What did you play ? Samourai, Oni or Kitsune ! ")
        print("Vanika choose her hand. . .")
        sleep(2)

        #Verification for user's entry :
        while choose != "Samourai" and choose != "Oni" and choose != "Kitsune":
            choose = input("Not valid, you need to choose between Samourai, Oni or Kitsune : ")
            sleep(3)

        #Compare user's hand against Vanika's hand
        if vanikaPlays == 1 and choose == "Oni":
            scoreVanika = scoreVanika + 1
            print(f"Vanika' Samourai slash {name}'s Oni !\nScore : {scorePlayer}/{scoreVanika}")

        elif vanikaPlays == 1 and choose == "Kitsune":
            scorePlayer = scorePlayer + 1
            print(f"{name}'s Kitsune crush {name}' Samourai !\nScore : {scorePlayer}/{scoreVanika}")

        elif vanikaPlays == 2 and choose == "Samourai":
            scorePlayer = scorePlayer + 1
            print(f"{name}' Samourai slash Vanika's Oni !\nScore : {scorePlayer}/{scoreVanika}")

        elif vanikaPlays == 2 and choose == "Kitsune":
            scoreVanika = scoreVanika + 1
            print(f"Vanika's Oni destroy {name}'s Kitsune !\nScore : {scorePlayer}/{scoreVanika}")

        elif vanikaPlays == 3 and choose == "Oni":
            scorePlayer = scorePlayer + 1
            print(f"{name}'s Oni destroy Vanika's Kitsune !\nScore : {scorePlayer}/{scoreVanika}")

        elif vanikaPlays == 3 and choose == "Samourai":
            scoreVanika = scoreVanika + 1
            print(f"Vanika's Kitsune crush {name}'s Samourai !\nScore : {scorePlayer}/{scoreVanika}")
        else:
            print("It's a draw.. \n")

#Who've win ??
scorePlayer = scorePlayer - scoreVanika
if scorePlayer > 0:
    print(f"\n\n[{name} WON] You've slayed Vanika !")
elif scorePlayer < 0:
    print("\n\n[Vanika WON] Vanika've crushed your hopes...")
else:

    print("\n\n[DRAW] It's a draw !")
