from Piece import Piece
from TextureLoader import TextureLoader


class Pawn(Piece):
    def __init__(self) -> None:
        super().__init__()

    def getAsset(self, texture_loader: TextureLoader):
        texture_loader.get_texture("pawn", self.white)