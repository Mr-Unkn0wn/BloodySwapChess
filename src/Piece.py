from typing import Tuple
from typing import List

from src.Board import Board


class Piece:
    position: Tuple[int, int]

    def __init__(self) -> None:
        pass # ToDo insert coordinates

    def generate_moves(self, board: Board) -> List[Tuple[int, int]]:
        pseudo_moves = self.generate_pseudo_legal_moves(board)
        moves = [move for move in pseudo_moves if self.is_legal_move(move, board)]
        return moves

    def generate_pseudo_legal_moves(self, board: Board) -> List[Tuple[int, int]]:
        pass

    def is_legal_move(self, move_to: Tuple[int, int], board: Board) -> bool:
        x, y = move_to
        if x < 0 or x > 7 or y < 0 or y > 7:
            return False

        return True

        # newBoard: apply move on board
        # board.is_valid

    def getAsset(self) -> str:
        """returns a string with the relative path to the piece asset
        must be overwritten by the specifig piece to get the specific asset
        """
        
        return "" 
