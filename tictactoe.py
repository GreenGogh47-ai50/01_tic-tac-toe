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
    return [["X", EMPTY, EMPTY], #REMEMBER TO CHANGE THIS BACK TO EMPTY
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    # x = 0
    # o = 0
    # pdb.set_trace()
    # for row in board:
    #     row.count("X") += x
    #     row.count("O") += O


    # runner uses ttt.X and ttt.O
    # Start with Terminal because that's the first method hit.

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    pdb.set_trace()


    # 1,2,3
    # 4,5,6
    # 7,8,9
    # Winning solutions are: rows the same, columns the same, & 1,5,9 or 3,5,6




    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
