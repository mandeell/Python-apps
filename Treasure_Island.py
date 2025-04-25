print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print('\nWhich direction do you want to go? left or right?')
direction_input = input('Enter l or L for left and r or R for right? \n')

if direction_input == 'l' or direction_input == 'L':
    print('\nDo you want to swim or wait?')
    swim_input = input('Enter s or S for swim and w or W for wait? \n')

    if swim_input == 'w' or swim_input == 'W':
        print('\nWhich door do you want to enter? Red or Blue or Yellow?')
        color_input = input('Enter r or R for red and b or B for blue and y or Y for yellow? \n')

        if color_input == 'y' or color_input == 'Y':
            print('\nYou Win!')
        elif color_input == 'r' or color_input == 'R':
            print('\nBurned by fire.\nGame Over.')
        elif color_input == 'b' or color_input == 'B':
            print('\nEaten by beasts.\nGame Over.')
        else:
            print('\nGame Over.')

    else:
        print('\nAttacked by trout.\nGame Over.')
else:
    print('\nFall into a hole.\nGame Over.')


