import math


# Initialize the board
def initialize_board():
    return [' ' for _ in range(9)]


# Print the board
def print_board(board):
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')
    print()


# Check if the current board state is a win for the given player
def is_winner(board, player):
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    return [player, player, player] in win_conditions


# Check if the board is full
def is_board_full(board):
    return ' ' not in board


# Get the available moves on the board
def get_available_moves(board):
    return [i for i, x in enumerate(board) if x == ' ']


# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    if is_winner(board, 'O'):
        return 1
    elif is_winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_available_moves(board):
            board[move] = 'O'
            eval = minimax(board, depth + 1, alpha, beta, False)
            board[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            board[move] = 'X'
            eval = minimax(board, depth + 1, alpha, beta, True)
            board[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


# Get the best move for the AI
def get_best_move(board):
    best_value = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = 'O'
        move_value = minimax(board, 0, -math.inf, math.inf, False)
        board[move] = ' '
        if move_value > best_value:
            best_value = move_value
            best_move = move
    return best_move


# Main game loop
def main():
    board = initialize_board()
    human_player = 'X'
    ai_player = 'O'

    while not is_board_full(board):
        print_board(board)

        if human_player == 'X':
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] != ' ':
                print("Invalid move! Try again.")
                continue
            board[move] = human_player
        else:
            print("AI is making a move...")
            move = get_best_move(board)
            board[move] = ai_player

        human_player, ai_player = ai_player, human_player

    print_board(board)

    # Check for winner after the board is full
    if is_winner(board, 'X'):
        print("Human wins!")
    elif is_winner(board, 'O'):
        print("AI wins!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    main()
