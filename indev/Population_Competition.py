from NN import *
from Gameboard import *
from Connect_Four import * 
import copy

#In the NN the value 1 is friendly piece and 2 is enemy, 0 is empty
def understandableBoard(board, color):
    c = copy.deepcopy(board)
    for x in range(len(c[0])):
        for y in range(c):
            if c[y][x] == None:
                c[y][x] = 0
            elif color == 0:
                c[y][x] += 1
            else:
                c[y][x] = 2 - c[y][x]  
    return c


def matchBetweenAI(modelA, modelB):
    board = initBoard()
    while(True):
        moveA = nnPrediction(understandableBoard(board,0),modelA)
        row = drop(board, moveA, 0)
        if fourConnectedCheck(board, row, moveA, 0):
            return 0
        moveB = nnPrediction(understandableBoard(board,1),modelB)
        row = drop(board, moveB, 1)
        if fourConnectedCheck(board, row, moveB, 1):
            return 1
        #Implement tie, TODO
        #if tie, reutrn another value. -1 perhaps
