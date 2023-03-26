import gameboard

def main():
    board = initBoard()
    drop(board, 1);

def twoPlayerGame():
    board = initBoard();
    while(True):
        try:
            print("Welcome to Connect Four! Press 0 for the player with 0 to begin and 1 for player 1 to begin");
            playerOneMove = int(input) == 0;
            break;
        except:
            print("Error, please only write the number and nothing else");

    while(True):
        printBoard(board);
        while(True):
            try:
                print("Choose column(0-6) to drop checker");
                column = int(input);
                if(column not in range(6)):
                    print("Something went wrong, try again");
                else:
                    break;
            except:
                print("Something went wrong, try again");
        
        if(playerOneMove):
            color = 0;
        else:
            color = 1;
        row = drop(board, column, color);
        if(fourConnectedCheck(board,row, column, color)):
            msg = "Player" + str(color+1) + " has won!";
            print(msg);
            break;
        playerOneMove = not playerOneMove;
