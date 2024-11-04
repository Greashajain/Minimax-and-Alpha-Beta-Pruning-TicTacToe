"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[None, None, None],
            [None, None, None],
            [None, None, None]]


def player(board):
    """
    calculate the no. of x and o in the board
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return O if x_count > o_count else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    i -> 0 to 2 
    j-> 0 to 2
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == None}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    """
    if action not in actions(board):
        raise ValueError("Invalid action")
    """
    if not isinstance(action, tuple) or len(action) != 2:
        raise ValueError(f"Invalid action format: {action}")
     
    new_board = [row[:] for row in board]
    current_player = player(board)
    new_board[action[0]][action[1]] = current_player
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell is not None for row in board for cell in row)
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0


def minimax(board, alpha=float('-inf'), beta=float('inf')):
    """
    Returns the optimal action for the current player on the board using minimax with alpha-beta pruning.
    """
    if terminal(board):
        return utility(board), None  # Return utility value and None for action

    current_player = player(board)

    # Initialize best action
    best_action = None

    if current_player == X:  # Maximize for X
        best_value = float('-inf')
        for action in actions(board):
            value, _ = minimax(result(board, action), alpha, beta)  # Recursively call minimax
            if value > best_value:
                best_value = value
                best_action = action
            alpha = max(alpha, best_value)  # Update alpha
            if beta <= alpha:  # Beta cutoff
                break
        return best_value, best_action  # Return best value and corresponding action
    else:  # Minimize for O
        best_value = float('inf')
        for action in actions(board):
            value, _ = minimax(result(board, action), alpha, beta)  # Recursively call minimax
            if value < best_value:
                best_value = value
                best_action = action
            beta = min(beta, best_value)  # Update beta
            if beta <= alpha:  # Alpha cutoff
                break
        return best_value, best_action