import sys
from gameboard import *

sys.path.append("..")

def twoPlayerGame():
    board = initBoard()
    while(True):
        try:
            print("Welcome to Connect Four! Press 0 for the player with 0 to begin and 1 for player 1 to begin")
            playerOneMove = int(input()) == 0
            break
        except:
            print("Error, please only write the number and nothing else")

    while(True):
        printGame(board)
        while(True):
            try:
                print("Choose column(1-7) to drop checker")
                column = int(input())
                if(column not in range(1,8)): #The user inputs 1 - 7 but in the calculus row value 0 is row the first row. Row 1.
                    print("Something went wrong, try again")
                else:
                    break
            except:
                print("Something went wrong, try again")
        
        if(playerOneMove):
            color = 0
        else:
            color = 1
        row = drop(board, column-1, color)
        print("Rowin: " + str(row) + "Column: " + str(column-1))
        if(fourConnectedCheck(board,row, column-1, color)):
            printGame(board)
            msg = "Player" + str(color+1) + " has won!"
            print(msg)
            break
        playerOneMove = not playerOneMove

def main():
    print("Hello")
    twoPlayerGame()

if __name__ == "__main__":
    main()