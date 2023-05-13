from typing import List, Tuple

from pygame import Surface

from Piece import Piece
from pieces import Bishop, King, Knight, Pawn, Queen, Rook
from pieces.TextureLoader import TextureLoader


class Board:
    board: List[Piece]  # 8x8 cells

    def __init__(self) -> None:
        """
        ugly solution, might fix later
        """
        self.board = [[None] * 8] * 8
        for i in range(8):
            self.board[1][i] = Pawn.Pawn((1, i), True, False)
            self.board[6][i] = Pawn.Pawn((6, i), False, False)
        self.board[0][0] = Rook.Rook((0, 0), True, False)
        self.board[7][0] = Rook.Rook((7, 0), False, False)
        self.board[0][7] = Rook.Rook((0, 7), True, False)
        self.board[7][7] = Rook.Rook((7, 7), False, False)

        self.board[0][1] = Knight.Knight((0, 1), True, True)
        self.board[0][6] = Knight.Knight((0, 6), True, True)
        self.board[7][1] = Knight.Knight((7, 1), False, True)
        self.board[7][6] = Knight.Knight((7, 6), False, True)

        self.board[0][2] = Bishop.Bishop((0, 2), True, False)
        self.board[7][2] = Bishop.Bishop((7, 2), False, False)
        self.board[0][5] = Bishop.Bishop((0, 5), True, False)
        self.board[7][5] = Bishop.Bishop((7, 5), False, False)

        self.board[7][3] = Queen.Queen((7, 3), False, False)
        self.board[0][3] = Queen.Queen((0, 3), True, False)

        self.board[7][4] = King.King((7, 4), False, False)
        self.board[0][4] = King.King((0, 4), True, False)
        

    def draw_board(self, screen: Surface, loader: TextureLoader):
        for row in self.board:
            for piece in row:
                if (piece != None):
                    texture = loader.get_texture(piece.get_name(), piece.get_white())
                    screen.blit(texture, dest = piece.get_position())



    def is_valid(self) -> bool:
        return False

    def generate_possible_moves(self, Piece) -> List[Tuple[int, int, int]] : 
        """@return Liste an allen tatsächlich möglichen (aber auch pseudo-möglichen) Bewegungen der Figur
        Format: (x, y, t) -> t == 0 ? Feld leer : Gegner auf dem Feld

        generiert eine Liste an möglichen und pseudo-möglichen Bewegungen einer Figur (Figur gibt eine Liste an allen relativen Bewegungsschemen zurück)
        entfernt: 
        - Positionen außerhalb des Boards
        - Positionen auf denen ein Verbündeter steht
        """
        # ToDo
        pass
