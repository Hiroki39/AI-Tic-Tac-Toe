"""
Tic Tac Toe Player
"""

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    diff = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X":
                diff += 1
            elif board[i][j] == "O":
                diff -= 1
    if diff == 0:
        return "X"
    return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] is not EMPTY:
        raise Exception("Invalid Move")

    board[i][j] = player(board)
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check if any row or column is filled with same pattern
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]

    # check diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # check if any row or column is filled with same pattern
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return True
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return True

    # check diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return True

    # check if board is full
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    if winner(board) == "O":
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    optimal_action = None
    if player(board) == "X":
        maximum_value = float("-inf")
        for action in actions(board):
            new_board = board_copy(board)
            # determine the utility with a recursive function
            curr_utility = calc_utility(result(new_board, action))
            if maximum_value < curr_utility:
                optimal_action = action
                maximum_value = curr_utility
    else:
        minimum_value = float("inf")
        for action in actions(board):
            new_board = board_copy(board)
            curr_utility = calc_utility(result(new_board, action))
            if minimum_value > curr_utility:
                optimal_action = action
                minimum_value = curr_utility
    return optimal_action


def calc_utility(board):
    # base case
    if terminal(board):
        return utility(board)
    if player(board) == "X":
        maximum_value = float("-inf")
        for action in actions(board):
            new_board = board_copy(board)
            curr_utility = calc_utility(result(new_board, action))
            if maximum_value < curr_utility:
                maximum_value = curr_utility
        return maximum_value
    else:
        minimum_value = float("inf")
        for action in actions(board):
            new_board = board_copy(board)
            curr_utility = calc_utility(result(new_board, action))
            if minimum_value > curr_utility:
                minimum_value = curr_utility
        return minimum_value


def board_copy(board):
    new_board = []
    for i in range(len(board)):
        curr_row = []
        for j in range(len(board[i])):
            curr_row.append(board[i][j])
        new_board.append(curr_row)
    return new_board
