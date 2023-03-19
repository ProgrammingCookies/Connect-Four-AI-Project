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

# written by Roy L.
# 2023-03-19
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

# written by Roy L.
# 2023-03-19
def clearscreen():
    clear = lambda: os.system('cls')
    clear()

# written by Axel L.
# 2023-03-19
def drop(board, column, color):
    nrRows = len(board);
    if(board[column][0] != None):
        return -1;
    for y in range(nrRows): #each row
        if(board[column][nrRows - 1 - y] != None):
            board[column][nrRows - y] = color;
            return nrRows - y;

# written by Axel L.
# 2023-03-19
#In this function we only need to check those 
def fourConnectedCheck(board, row, column, color):
    nrRows = len(board) - 1;
    nrColumns = len(board[0]) - 1;
    #To the right
    nrConnected = 1;
    for x in range(nrColumns - column):
        if(board[column + x][row] == color):
            nrConnected += 1;
            if(nrConnected == 4):
                return True;
            else:
                break;
        else:
            break;
    #To the left
    nrConnected = 1;
    for x in range(column):
        if(board[column - x][row] == color):
            nrConnected += 1;
            if(nrConnected == 4):
                return True;
            else:
                break;
        else:
            break;
    #South West
    nrConnected = 1;
    z = min(column, row);
    for x in range(z):
        if(board[column - x][row - x] == color):
            nrConnected += 1;
            if(nrConnected == 4):
                return True;
            else:
                break;
        else:
            break;
    #South East
    nrConnected = 1;
    z = min(nrColumns - column, row);
    for x in range(z):
        if(board[column + x][row - x] == color):
            nrConnected += 1;
            if(nrConnected == 4):
                return True;
            else:
                break;
        else:
            break;
    return False;
    

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
