from pygame import Surface

from src.Piece import Piece
from typing import List
import src.pieces as piece


class Board:
    board: List[Piece]  # 8x8 cells

    def __init__(self) -> None:
        """
        ugly solution, might fix later
        """
        board = [[None] * 8] * 8
        for i in range(8):
            board[1, i] = piece.Pawn() # ToDo
            board[6, i] = piece.Pawn()
        board[0, 0] = piece.Rook()
        board[7, 0] = piece.Rook()
        board[0, 7] = piece.Rook()
        board[7, 7] = piece.Rook()

        board[0, 1] = piece.Knight()
        board[0, 6] = piece.Knight()
        board[7, 1] = piece.Knight()
        board[7, 6] = piece.Knight()

        board[0, 2] = piece.Bishop()
        board[7, 2] = piece.Bishop()
        

    def draw_board(self, screen: Surface):
        for row in self.board:
            for element in row:
                texture = element.get_asset()
                screen.blit(texture)



    def is_valid(self) -> bool:
        return False
