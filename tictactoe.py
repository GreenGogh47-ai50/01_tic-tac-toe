"""
Tic Tac Toe Player
"""

import math
import pdb
import random

# pdb.set_trace()

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    # return [[X, O, X], #This set is for texting. O's next move. (0,1) is the correct next move.
    #         [O, O, X],
    #         [EMPTY, X, X]]

    # return [[X, O, EMPTY],
    #         [X, O, X],
    #         [O, O, X]]

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    *X always goes first
    """

    x = 0
    o = 0

    for row in board:
        x += row.count("X")
        o += row.count("O")

    return O if x>o else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # (Pdb) board
    # [['X', None, 'X'], ['X', 'O', None], ['O', None, None]]
    # (Pdb) for row in board:
    # ...     for cell in row:
    # ...             print(board[row][cell]) - not the whole row - the row number

    # (Pdb) for row in range(len(board)):
    # ...     for cell in range(len(row)):
    # ...             print(row, cell)
    # ...   
    # *** TypeError: object of type 'int' has no len()

    # (Pdb)     for row in range(len(board)):
    # ...           for cell in range(len(board[row])):
    # ...               if board[row][cell] != None:
    # ...                   moves.append((row, cell))
    # ...   
    # (Pdb) moves
    # [(0, 0), (0, 2), (1, 0), (1, 1), (2, 0)]


    actions = []

    for row in range(len(board)):
        for cell in range(len(board[row])):
            if board[row][cell] == None:
                actions.append((row, cell))

    return actions

    # refactor to use (i,j) like in the instructions and in runner:88 (board[i][j])




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # (Pdb) moves (actions)
    # [(0, 1), (1, 2), (2, 1), (2, 2)]
    # (Pdb) board
    # [['X', None, 'X'], ['X', 'O', None], ['O', None, None]]
    # (Pdb)

    # (Pdb) board[0]
    # ['X', None, 'X']
    # (Pdb) board[0][0]
    # 'X'
    # (Pdb) board[0][1]
    # (Pdb) board[0][1] = moves[0]
    # (Pdb) board
    # [['X', (0, 1), 'X'], ['X', 'O', None], ['O', None, None]]
    # lol - no

    # (Pdb) board[row][cell] = ttt.player(board) /// ttt because pry (Pdb) is in the runner.
    # (Pdb) board
    # [['X', 'O', 'X'], ['X', 'O', None], ['O', None, None]]

    current_player = player(board) #ttt.pyaler(board) while in pry (Pdb)
    row = action[0]
    cell = action[1]

    board[row][cell] = current_player
    return board

    # pdb.set_trace()


def winner(board):
    """
    Returns the winner of the game, if there is one.
    *runner:101 It has to terminate before a winner is decided
    *runner:106 it's expecting a string "X" or "O"
    **Do the terminal method before this**
    """
    # raise NotImplementedError
    #  return player(board) -- nope that returns the opposite.

    if player(board) == X:
        return O
    else:
        return X

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    The game is over if there are no legal moves/actions
    Or if there's a match of 3
    """

    # 1,2,3
    # 4,5,6
    # 7,8,9
    # Winning solutions are: rows the same, columns the same, & 1,5,9 or 3,5,6

    if actions(board) == []:
        return True

    # Rows
    # (Pdb)     for row in board:
    # ...           if row[0] == row[1] == row[2] != None:
    # ...               print("true") # True
    # ...           else:
    # ...               print("false") # return False
    # ...   
    # true
    # false
    # false
    # (Pdb) 

    for row in board:
        if row[0] == row[1] == row[2] != None:
            return True

    # #Columns Notes
    # if board[0,0] == board[0,1] == board[0,2]!= None:
    #     print("true")
    # if board[0,0] == board[0,1] == board[0,2]!= None:
    #     print("true")
    # if board[0,0] == board[0,1] == board[0,2]!= None:
    #     print("true")
    # else:
    #     print("false")

    # Same issue, can't call tuples in this way.

    #Columns
    for cell in range(3):
        if board[0][cell] == board[1][cell] == board[2][cell] != None:
            return True

    #Diagonals
    if board[0][0] == board[1][1] == board[2][2] != None:
        return True

    if board[0][2] == board[1][1] == board[2][0] != None:
        return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    I think this would just be a case statement
    Do this after winner
    """
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    This will be done last.
    """
    return random.choice(actions(board))
