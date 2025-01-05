
from django.db import models

class Game(models.Model):
    board = models.CharField(max_length=9, default="         ")  # A 3x3 Tic-Tac-Toe grid as a string
    current_turn = models.CharField(max_length=1, default='X')  # X starts the game

    def __str__(self):
        return f"Game with board {self.board} and current turn {self.current_turn}"

# Create your models here.
