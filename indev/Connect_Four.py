import sys
from Gameboard import *

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
            userinput = input("Choose column(1-7) to drop checker. Write 'quit' to exit: ")
            if userinput == "quit":
                break
            try:
                column = int(userinput)
                if((column not in range(1,8)) or (board[0][column - 1] is not None)): #The user inputs 1 - 7 but in the calculus row value 0 is row the first row. Row 1.
                    print("Something went wrong, try again")
                else:
                    break
            except ValueError:
                print("Invalid input.")
        
        if userinput == "quit":
            break
        elif(playerOneMove):
            color = 0
        else:
            color = 1
        row = drop(board, column, color)
        print("Rowin: " + str(row) + " Column: " + str(column-1))
        if(fourConnectedCheck(board,row, column, color)):
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
