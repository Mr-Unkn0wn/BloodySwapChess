from pygame import Surface

from typing import List
from typing import Tuple
from pieces import Bishop, King, Knight, Pawn, Queen, Rook
from pieces.TextureLoader import TextureLoader


class Piece:
    position: Tuple[int, int]
    white: bool

    def __init__(self) -> None:
        pass # ToDo insert coordinates

    def generate_moves(self, board) -> List[Tuple[int, int]]:
        pseudo_moves = self.generate_pseudo_legal_moves(board)
        moves = [move for move in pseudo_moves if self.is_legal_move(move, board)]
        return moves

    def generate_pseudo_legal_moves(self, board) -> List[Tuple[int, int]]:
        pass

    def is_legal_move(self, move_to: Tuple[int, int], board) -> bool:
        x, y = move_to
        if x < 0 or x > 7 or y < 0 or y > 7:
            return False

        return True

        # newBoard: apply move on board
        # board.is_valid

    def getAsset(self, texture_loader: TextureLoader):
        """returns a string with the relative path to the piece asset
        must be overwritten by the specifig piece to get the specific asset
        """
        
        return "" 

class Board:
    board: List[Piece]  # 8x8 cells

    def __init__(self) -> None:
        """
        ugly solution, might fix later
        """
        self.board = [[None] * 8] * 8
        for i in range(8):
            self.board[1, i] = Pawn() # ToDo
            self.board[6, i] = Pawn()
        self.board[0, 0] = Rook()
        self.board[7, 0] = Rook()
        self.board[0, 7] = Rook()
        self.board[7, 7] = Rook()

        self.board[0, 1] = Knight()
        self.board[0, 6] = Knight()
        self.board[7, 1] = Knight()
        self.board[7, 6] = Knight()

        self.board[0, 2] = Bishop()
        self.board[7, 2] = Bishop()
        self.board[0, 5] = Bishop()
        self.board[7, 5] = Bishop()

        self.board[7, 3] = Queen()
        self.board[0, 3] = Queen()

        self.board[7, 4] = King()
        self.board[0, 4] = King()
        

    def draw_board(self, screen: Surface):
        for row in self.board:
            for element in row:
                texture = element.get_asset()
                screen.blit(texture)



    def is_valid(self) -> bool:
        return False

