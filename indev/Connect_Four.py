

def main():
    board = int[7][6];
    drop(board, 1);


def drop(board, column, color):
    nrRows = len(board);
    if(board[column][0] != None):
        return -1;
    for y in range(nrRows): #each row
        if(board[column][nrRows - 1 - y] != None):
            board[column][nrRows - y] = color;
            return nrRows - y;

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


def twoPlayerGame():
    board = initializeBoard();
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










