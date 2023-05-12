from pygame import Surface

import Piece as p
from typing import List
import pieces as piece


class Board:
    board: List[p.Piece]  # 8x8 cells

    def __init__(self) -> None:
        """
        ugly solution, might fix later
        """
        self.board = [[None] * 8] * 8
        for i in range(8):
            self.board[1, i] = piece.Pawn() # ToDo
            self.board[6, i] = piece.Pawn()
        self.board[0, 0] = piece.Rook()
        self.board[7, 0] = piece.Rook()
        self.board[0, 7] = piece.Rook()
        self.board[7, 7] = piece.Rook()

        self.board[0, 1] = piece.Knight()
        self.board[0, 6] = piece.Knight()
        self.board[7, 1] = piece.Knight()
        self.board[7, 6] = piece.Knight()

        self.board[0, 2] = piece.Bishop()
        self.board[7, 2] = piece.Bishop()
        self.board[0, 5] = piece.Bishop()
        self.board[7, 5] = piece.Bishop()

        self.board[7, 3] = piece.QUEEN()
        self.board[0, 3] = piece.QUEEN()

        self.board[7, 4] = piece.KING()
        self.board[0, 4] = piece.KING()
        

    def draw_board(self, screen: Surface):
        for row in self.board:
            for element in row:
                texture = element.get_asset()
                screen.blit(texture)



    def is_valid(self) -> bool:
        return False
