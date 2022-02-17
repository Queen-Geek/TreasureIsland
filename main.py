print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')

print("Welcome to Treasure Island!\n")
print("Your mission is to find the tresure.\n")
direction = (input("You're at a cross roads. \nDo you want to go 'left' or 'right'?\n")).lower()

if direction == "left":

    wait = input("You have arrived at a lake. There is an island in the middle. \nDo you want to 'swim' to the island or 'wait' for a boat?\n").lower()
    if wait == "wait":
        print("Good pick. You may continue.")
        color = input("You have arrived at the island unharmed. The is a house with 3 doors: \none 'red', one 'yellow', and one 'blue'. Which color do you choose?\n").lower()
        if color == "yellow":
            print("You have found the tresure! You win!")
        elif color == "blue":
            print("You were eaten by beats. Game over.")
        elif color == "red":
            print("You were burned by fire. Game over.")
        else:
            print("Game over.")
    else:
        print("You were attacked by trout. Game over.")
        
else:
    print("You fell into a hole. Game over.")