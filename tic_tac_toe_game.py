#tic_tac_toe
import numpy as np
import random
from time import sleep

def create_board():
    return np.array([[0,0,0],
                     [0,0,0],
                     [0,0,0]])
def squarePos(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i,j] == 0:
                l.append((i,j))
    #print(l)
    return l

def play(board,player):
    poss = squarePos(board)
    squareIndex = random.randint(0,len(poss)-1)
    #print(poss)
    #print(squareIndex)
    board[poss[squareIndex]] = player

def empty(board):
    pos = squarePos(board)
    if(len(pos) == 0):
        return True
    return False
# make win conditions
def row_win(board,playerList):
    rowWin = True
    for i in range(len(board)):
        for j in range(1,len(board)):
            rowCheck = board[i][0]
            if(board[i][j] == )

#driving code
playerList = [1,2]
board = create_board()
print(board)
while not empty(board):
    play(board,playerList[0])
    print(board)
    sleep(2)
    if empty(board):
        break
    play(board,playerList[1])
    print(board)
    sleep(2)

    
    


    


    