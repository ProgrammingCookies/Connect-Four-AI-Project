from NN import *
from Gameboard import *
from Connect_Four import * 
import copy

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
