#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# chy
class TicTacToe:

    def __init__(self):
        """Start a new game"""
        self._board = [[' '] * 3 for i in range(3)]
        self._player = 'X'

    def mark(self, i, j):
        """Put and X or O mark at position (i, j) for next player's turn"""
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError('Invalid board position')
        if self._board[i][j] != ' ':
            raise ValueError('Board position occupied')
        if self.winner() is not None:
            raise ValueError('Game is already')
        self._board[i][j] = self._player
        if self._player == 'X':
            self._player = 'O'
        else:
            self._player = 'X'

    def _is_win(self, mark):
        """Check whether the board configuration is a win for the given player"""
        board = self._board
        return (
            mark == board[0][0] == board[0][1] == board[0][2] or
            mark == board[1][0] == board[1][1] == board[1][2] or
            mark == board[2][0] == board[2][1] == board[2][2] or
            mark == board[0][0] == board[1][0] == board[2][0] or
            mark == board[0][1] == board[1][1] == board[2][1] or
            mark == board[0][2] == board[1][2] == board[2][2] or
            mark == board[0][0] == board[1][1] == board[2][2] or
            mark == board[0][2] == board[1][1] == board[2][0]
        )

    def winner(self):
        """Return mark of winning player, or None to indicate a tie"""
        for mark in 'XO':
            if self._is_win(mark):
                return mark
        return None

    def __str__(self):
        """Return string representation of current game board"""
        rows = ["丨".join(self._board[i]) for i in range(3)]
        return '\n------\n'.join(rows)


if __name__ == "__main__":
    game = TicTacToe()
    game.mark(1, 1)
    game.mark(0, 2)
    game.mark(2, 2)
    game.mark(0, 0)
    game.mark(0, 1)
    game.mark(2, 1)
    game.mark(1, 2)
    game.mark(1, 0)
    game.mark(2, 0)

    print(game)
    winner = game.winner()
    print(winner)

