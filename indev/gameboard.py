import os
import time

# create a 7 x 6 game board
gameboard = [[None, None, None, None, None, None, None],
[None, None, None, None, None, None, None],
[None, None, None, None, 0, None, None],
[None, None, None, None, 1, None, None],
[None, None, None, None, 0, None, None],
[None, None, None, None, 1, None, None]]

gameboard2 = [[None, None, None, None, None, None, None],
[None, None, None, None, 1, None, None],
[None, None, None, None, 0, None, None],
[None, None, None, None, 1, None, None],
[None, None, None, None, 0, None, None],
[None, None, None, None, 1, None, None]]

gameboard3 = [[None, None, None, None, 0, None, None],
[None, None, None, None, 1, None, None],
[None, None, None, None, 0, None, None],
[None, None, None, None, 1, None, None],
[None, None, None, None, 0, None, None],
[None, None, None, None, 1, None, None]]

def printgame(gameboard):
    print(" --- --- --- --- --- --- --- ")
    print(" ", end = '')
    for y in range(6):
        for x in range(7):
            if(x == 6):
                if(y != 5):
                    if(gameboard[y][x] is None):
                        print("   ")
                        print(" --- --- --- --- --- --- --- ")
                        print(" ", end = '')
                    elif(gameboard[y][x] == 0):
                        print(" O ")
                        print(" --- --- --- --- --- --- --- ")
                        print(" ", end = '')
                    elif(gameboard[y][x] == 1):
                        print(" X ")
                        print(" --- --- --- --- --- --- --- ")
                        print(" ", end = '')
                else:
                    if(gameboard[y][x] is None):
                        print("   ")
                        print(" --- --- --- --- --- --- --- ")
                    elif(gameboard[y][x] == 0):
                        print(" O ")
                        print(" --- --- --- --- --- --- --- ")
                    elif(gameboard[y][x] == 1):
                        print(" X ")
                        print(" --- --- --- --- --- --- --- ")
            else:
                if(gameboard[y][x] is None):
                    print("   |", end = '')
                elif(gameboard[y][x] == 0):
                    print(" O |", end = '')
                elif(gameboard[y][x] == 1):
                    print(" X |", end = '')

def clearscreen():
    clear = lambda: os.system('cls')
    clear()

# testkod, ta bort
clearscreen()
printgame(gameboard)
time.sleep(2)
clearscreen()
printgame(gameboard2)
time.sleep(2)
clearscreen()
printgame(gameboard3)
time.sleep(2)
clearscreen()
print("hello")

# visualization of the gameboard
# --- --- --- --- --- --- ---
#    |   |   |   |   |   |   
# --- --- --- --- --- --- ---
#    |   |   |   |   |   |   
# --- --- --- --- --- --- ---
#    |   |   |   |   |   |   
# --- --- --- --- --- --- ---
#    |   |   |   |   |   |   
# --- --- --- --- --- --- ---
#    |   |   |   |   |   |   
# --- --- --- --- --- --- ---
#    |   |   |   |   |   |   
# --- --- --- --- --- --- ---