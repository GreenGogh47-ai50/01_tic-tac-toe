"""
Tic Tac Toe Player
"""

import math
import pdb

# pdb.set_trace()

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[X, EMPTY, X], #REMEMBER TO CHANGE THIS BACK TO EMPTY
            [X, O, EMPTY],
            [O, EMPTY, EMPTY]]

    # return [[EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY]]


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
    *i is the board, and j is the move runner:121
    *this method isn't used in the runner - so it's options for the minimax
    """
    raise NotImplementedError

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
    *i is the board, and j is the move runner:121

    board = [['X', None, 'X'], ['X', 'O', None], ['O', None, None]]
    action = (0,1)
    return [['X', 'X', 'X'], ['X', 'O', None], ['O', None, None]]

    """
    # (Pdb) moves (actions)
    # [(0, 1), (1, 2), (2, 1), (2, 2)]
    # (Pdb) board
    # [['X', None, 'X'], ['X', 'O', None], ['O', None, None]]
    # (Pdb)



    pdb.set_trace()



def winner(board):
    """
    Returns the winner of the game, if there is one.
    *runner:101 It has to terminate before a winner is decided
    *runner:106 it's expecting a string "X" or "O"
    **Do the terminal method before this**
    """
    # raise NotImplementedError


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
    # Just because we're checking that the game is over first doesn't necessarily mean
    # That's the place to start

    # For now I'll just have the game over condition as:
    if None not in board:
        return False
    else:
        return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    I think this would just be a case statement
    Do this after winner
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    This will be done last.
    """
    raise NotImplementedError
