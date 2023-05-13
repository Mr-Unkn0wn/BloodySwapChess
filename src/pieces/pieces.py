from Piece import Piece


class Bishop(Piece):
    def __init__(self, position, white, jumpable) -> None:
        super().__init__(position, white, jumpable)

    def get_name(self) -> str:
        return "bishop"

class King(Piece):
    def __init__(self, position, white, jumpable) -> None:
        super().__init__(position, white, jumpable)

    def get_name(self) -> str:
        return "king"
    
class Pawn(Piece):
    def __init__(self, position, white, jumpable) -> None:
        super().__init__(position, white, jumpable)

    def get_name(self) -> str:
        return "pawn"
    
class Queen(Piece):
    def __init__(self, position, white, jumpable) -> None:
        super().__init__(position, white, jumpable)

    def get_name(self) -> str:
        return "queen"
    
class Knight(Piece):
    def __init__(self, position, white, jumpable) -> None:
        super().__init__(position, white, jumpable)

    def get_name(self) -> str:
        return "knight"
    
class Rook(Piece):
    def __init__(self, position, white, jumpable) -> None:
        super().__init__(position, white, jumpable)

    def get_name(self) -> str:
        return "rook"