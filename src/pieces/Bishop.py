from src.Piece import Piece
from src.pieces.TextureLoader import TextureLoader


class Bishop(Piece):
    def __init__(self) -> None:
        super().__init__()

    def getAsset(self, texture_loader: TextureLoader):
        texture_loader.get_texture("bishop", self.white)