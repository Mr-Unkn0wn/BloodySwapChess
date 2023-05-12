from typing import Tuple
from typing import List

import Board as b
from pieces.TextureLoader import TextureLoader


class Piece:
    position: Tuple[int, int]
    white: bool

    def __init__(self) -> None:
        pass # ToDo insert coordinates

    def generate_moves(self, board: b.Board) -> List[Tuple[int, int]]:
        pseudo_moves = self.generate_pseudo_legal_moves(board)
        moves = [move for move in pseudo_moves if self.is_legal_move(move, board)]
        return moves

    def generate_pseudo_legal_moves(self, board: b.Board) -> List[Tuple[int, int]]:
        pass

    def is_legal_move(self, move_to: Tuple[int, int], board: b.Board) -> bool:
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
