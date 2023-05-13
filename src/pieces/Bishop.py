from Piece import Piece


class Bishop(Piece):
    def __init__(self, position, white, jumpable) -> None:
        super().__init__(position, white, jumpable)

    def get_name(self) -> str:
        return "bishop"
