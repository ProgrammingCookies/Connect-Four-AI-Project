import os
import time

# create a 7 x 6 game board
def initBoard():
    gameboard = [[None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None]]
    return gameboard

# written by Roy L.
# 2023-03-19
def printGame(gameboard):
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
def clearScreen():
    clear = lambda: os.system('cls')
    clear()

# written by Axel L. & Roy L.
# 2023-03-19
def drop(board, column, color):
    nrRows = len(board)
    if(board[0][column - 1] != None):
        return -1
    for y in range(nrRows - 1): #each row
        if(board[y + 1][column - 1] != None):
            board[y][column - 1] = color
            return nrRows - y
    board[nrRows - 1][column - 1] = color
    return nrRows - 1


# written by Axel L.
# 2023-03-19
#Checks if someone has won, row and column arguments are entered as 0-5/0-6
def fourConnectedCheck(board, row, column, color):
    nrRows = len(board)
    nrColumns = len(board[0])
    #To the right
    nrConnected = 1
    for x in range(1,nrColumns - column):
        if(board[row - 1][column - x] == color):
            nrConnected += 1
            if(nrConnected == 4):
                return True
        else:
            break
    #To the left
    nrConnected = 1
    for x in range(1,column):
        if(board[row - 1][column - x] == color):
            nrConnected += 1
            if(nrConnected == 4):
                return True
        else:
            break
    #South West
    nrConnected = 1
    z = min(column, nrRows - row)
    for x in range(1,z):
        if(board[row + x][column - x] == color):
            nrConnected += 1
            if(nrConnected == 4):
                return True
        else:
            break
    #South East
    nrConnected = 1
    z = min(nrColumns - column, nrRows - row)
    for x in range(1,z):
        if(board[row + x][column + x] == color):
            nrConnected += 1
            if(nrConnected == 4):
                return True
        else:
            break
    #Down
    nrConnected = 1
    for x in range(1,nrRows - row):
        if(board[row+x][column - x] == color):
            nrConnected += 1
            if(nrConnected == 4):
                print("")
                return True
        else:
            break
    return False
    
# visualization of an empty gameboard
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
