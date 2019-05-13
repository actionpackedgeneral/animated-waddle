# -*- coding: utf-8 -*-
"""
Created on Sun May 12 17:31:58 2019

@author: agul
"""
import tic_tac_toe_game

playerList = [1,2]
board = create_board()
print(board)
while not empty(board):
    playerList = [1,2]
    play(board,playerList[0])
    print(board)
    sleep(2)
    if empty(board):
        break
    play(board,playerList[1])
    print(board)
    sleep(2)
    
    
    
    