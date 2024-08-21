#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    board = request.session.get('board', [''] * 9)
    message = request.session.get('message', 'Player X\'s turn')
    winner = check_winner(board)

    if winner:
        message = f"Player {winner} wins!"
    elif '' not in board:
        message = "It's a tie!"
    board = [''] * 9  # Example board with 9 empty slots
    context = {
        'board': board,
        'range': range(3),  # Add a range of 3 for iteration
    }
    return render(request, 'tictactoe/index.html', context)

def make_move(request, position):
    board = request.session.get('board', [''] * 9)
    current_player = request.session.get('current_player', 'X')
    if board[position] == '' and not check_winner(board):
        board[position] = current_player
        current_player = 'O' if current_player == 'X' else 'X'
        request.session['board'] = board
        request.session['current_player'] = current_player

    return index(request)

def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6],  # diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] and board[combo[0]] == board[combo[1]] == board[combo[2]]:
            return board[combo[0]]
    return None

def reset(request):
    request.session['board'] = [''] * 9
    request.session['current_player'] = 'X'
    request.session['message'] = 'Player X\'s turn'
    return index(request)
