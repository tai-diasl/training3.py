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
*******************************************************************************
''')

print("Welcome to Monte Cristo Island.\nYour mission is to find the Treasure of Spada.\n")

again = "yes"

while again == "yes":
    left_right = input(
        "You enter a cave and now you are at a crossroads. Where do you want to go? Type 'left' or 'right'\n")
    if left_right == 'left':
        print(
            "You hear the voice of Count Mondego, who has followed you to a certain point and is also inside the cave.")
        back_continue = input("What do you want to do? Type 'return' or 'continue'\n")
        if back_continue == "return":
            print("You arrive at a lake with beautiful turquoise waters.")
            jump_walk = input("Do you jump into the water or keep walking through the cave? Type 'jump' or 'walk'.\n")
            if jump_walk == "walk":
                print(
                    "You keep walking, and see another lake with not so crystal clear water and in this one, there are some sharp rocks.")
                final = input(
                    "Do you go into the water, go back to the other lake, or continue walking through the cave? Type 'go', 'go back' or 'walk'.\n")
                if final == "go":
                    print(
                        "*** You find the treasure! You take the chests from the bottom of the lake and put them inside the boat!")
                    print("You join Mercédès, Albert, Jacopo and start a new journey!")
                    print("Good Luck! ***")
                elif final == "go back":
                    print("Oh no, the lake is shallower than it looked... you hurt yourself on a rock. GAME OVER!")
                else:
                    print("You meet Count Mondego and are sent to the Chatêau d'If again... GAME OVER!")
            else:
                print("Oh no, the lake is shallower than it looked... you hurt yourself on a rock. GAME OVER!")
        else:
            print("You are captured by Count Mondego and sent back to the Chatêau d'If...\nGAME OVER!")
    else:
        print("Oh no! There is a hole just around the corner. You fell in there. \nGAME OVER!")
    again = input("\n\nLet's try again? Type 'yes' or 'no': ")