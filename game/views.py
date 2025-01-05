from django.shortcuts import render
from django.http import JsonResponse
from .models import Game

# A function to initialize or reset the game
def new_game(request):
    game = Game.objects.create()  # create a new game
    return JsonResponse({'game_id': game.id, 'board': game.board, 'current_turn': game.current_turn})

# A function to handle player moves
def make_move(request, game_id, position):
    game = Game.objects.get(id=game_id)
    if game.board[position] != ' ':
        return JsonResponse({'error': 'Invalid move'})
    
    board = list(game.board)
    board[position] = game.current_turn
    game.board = ''.join(board)
    game.current_turn = 'O' if game.current_turn == 'X' else 'X'
    game.save()

    return JsonResponse({'board': game.board, 'current_turn': game.current_turn})

# Function to render the game interface
def game_view(request):
    return render(request, 'game/index.html')
