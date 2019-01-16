# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:53:28 2018

@author: harpal
"""
from IPython.display import clear_output

'''x=input()
print("Input value is:", x) '''
'''clear_output()  work in jupyter'''
lst=[]
def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
 
lst=['X']*10    
#display_board(lst)

def display_board1(board):
    print('   |   |')
    print(' '+ board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+ board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+ board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    
display_board1(lst)

def player_input():
    '''i=1
    l1=[]
    while(i<10):
        d=input()
        l1.append(d)
        i+=1    
    print(l1)'''

l2=['x', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
player_input()    
display_board1(l2)

def player_input(): 
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O?').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker   

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
     (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
     (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom        
     (board[1] == mark and board[5] == mark and board[9] == mark) or # across the accross left
     (board[7] == mark and board[5] == mark and board[3] == mark) or # across the cross
     (board[7] == mark and board[4] == mark and board[1] == mark) or # across the left         
     (board[8] == mark and board[5] == mark and board[2] == mark) or # across the middle column
     (board[9] == mark and board[6] == mark and board[3] == mark)) # across the right columns

import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    
def space_check(board, position):  
    return board[position] == ' '    
    
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True   
    
def player_choice(board):
    # Using strings because of raw_input
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Choose your next position: (1-9) ')
    return int(position)

def replay(): 
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break    
    
    