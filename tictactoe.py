"""
Tic Tac Toe Player
"""

import math
import pdb
import random
import copy

# pdb.set_trace()

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    # return [['X', EMPTY, 'X'],
    #         ['X', 'O', EMPTY],
    #         ['O', EMPTY, EMPTY]]

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

    return O if x > o else X


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

    current_player = player(board)  # ttt.pyaler(board) while in pry (Pdb)
    # deep copy to prevent mutation while minimax iterates.
    new_board = copy.deepcopy(board)
    row = action[0]
    cell = action[1]

    new_board[row][cell] = current_player
    return new_board

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

# This was not the move.
    # if player(board) == X:
    #     return O
    # else:
    #     return X

    for row in board:
        if row[0] == row[1] == row[2] != None:
            return row[0]

    # Columns
    for cell in range(3):
        if board[0][cell] == board[1][cell] == board[2][cell] != None:
            return board[0][cell]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != None:
        return board[0][2]


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

    # Columns Notes
    # if board[0,0] == board[0,1] == board[0,2]!= None:
    #     print("true")
    # if board[0,0] == board[0,1] == board[0,2]!= None:
    #     print("true")
    # if board[0,0] == board[0,1] == board[0,2]!= None:
    #     print("true")
    # else:
    #     print("false")

    # Same issue, can't call tuples in this way.

    # Columns
    for cell in range(3):
        if board[0][cell] == board[1][cell] == board[2][cell] != None:
            return True

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != None:
        return True

    if board[0][2] == board[1][1] == board[2][0] != None:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    You may assume `utility` will only be called on a `board`
    if `terminal(board)` is `True`. (oh man thank you.)
    """

    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
- [x] If the `board` is a terminal board, the `minimax` function should return `None`.
- [x] The `minimax` function should take a `board` as input, and return
    the OPTIMAL MOVE for the player to move on that `board`.
- [x] The move returned should be the optimal action `(i, j)`
    that is one of the allowable `actions` on the `board`.
    If multiple moves are equally optimal,
    any of those moves is acceptable.

    Returns the OPTIMAL MOVE for the CURRENT PLAYER on the board.
    """
    # # randomizer so I could check if everything else worked.
    # return random.choice(actions(board))

    # "If the `board` is a terminal board, the `minimax` function should return `None`."
    if terminal(board):
        return None

    # 1. Who's playing?
    current_player = player(board)

    # 2. Current players objective
    if current_player == "X":
        # The best utility STARTS at -infinity for X
        best_utility = float('-inf')
    else:
        # The best utility STARTS at infinity for O
        best_utility = float('inf')

    # Tracking the optimal move
    optimal_move = EMPTY

    # 3. What are all the possible moves? actions(board)
    for action in actions(board):
        # 4. What does the board look like after a move? result(board, action)
        next_board = result(board, action)

        # 5. What is the utility of THAT board, then that board, then that board?
        # Some kind of recursion like Dr. Yu said. It needs to be able to call itself so it needs to be its own function.
        # if terminal(next_board):
        #     return utility(board)

        # if current_player == X:

        value = minimax_utility(next_board)

        if current_player == X:
            if value > best_utility:
                # The best utility becomes the new result of the minimax_utility (starting at -infinity)
                best_utility = value
                # The optimal move becomes THAT action (starting at infinity)
                optimal_move = action
        else:
            if value < best_utility:
                best_utility = value
                optimal_move = action

    # 6. Which is the best move?
    return optimal_move


def minimax_utility(board):
    if terminal(board):
        return utility(board)

    current_player = player(board)

    if current_player == X:
        # FROM CLASS NOTES
        # v = MAX(v, MIN-VALUE(RESULT(state, action)))
        # 	return v
        v = float('-inf')
        for action in actions(board):
            # pick the value CLOSEST to 1 (furthest from -inf)
            v = max(v, minimax_utility(result(board, action)))
            print(f"Evaluating move {action} → score: {v}")
        return v
    else:
        v = float('inf')
        for action in actions(board):
            # pick the value CLOSEST to -1 (furthest from +inf)
            v = min(v, minimax_utility(result(board, action)))
            print(f"Evaluating move {action} → score: {v}")
        return v


# 1. Who's playing? player(board)
#  2. What's their objective?
# 3. What are all the possible moves? actions(board)
# 4. What does the board look like after a move? result(board, action)
# 5. What is the utility of THAT board?
# Is the game over?
# If the game is over, what's the score? utility(board)

"""
In order to figure out your move, you have to know what the opponent will do next,
meaning you need to know what you will do next,
meaning you need to know what they will do next,
ect until the game ends. And depending on how that tree resolves,
it's either a win, loss, or tie (1, -1, or 0).
The max player (x) wants to maximize the score,
and the min player tries to minimize it.

x wants to beat negative infinity
and o wants to be infinity
I need another method so I can call it recursively

    # FROM CLASS NOTES
    # v = MAX(v, MIN-VALUE(RESULT(state, action)))
    # 	return v
"""