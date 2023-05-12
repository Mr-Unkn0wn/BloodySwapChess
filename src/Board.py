from src.Piece import Piece
from typing import List


class Board:
    board: List[Piece]  # 8x8 cells

    def is_valid(self) -> bool:
        return False
