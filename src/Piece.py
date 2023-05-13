from typing import Tuple
from typing import List

class Piece:
    """Definiert eine Figur
    Definiert Bewegungsmuster in abhängigkeit der Position und ob die Figur über andere Figuren springen kann
    """
    position: Tuple[int, int]
    white: bool
    jumpable: bool # for knight to calc possible moves

    def __init__(self, position: Tuple[int, int], white: bool, jumpable: bool):
        self.position = position
        self.white = white
        self.jumpable = jumpable

    def get_relative_moves() -> List[Tuple[int, int]]:
        """@return List mit allen relativen Punkten, von denen aus die Figur hin kann
        Betrachtet nicht, ob weitere Figuren im Weg stehen
        """
        pass

    def get_name(self) -> str:
        return ""
    
    def get_position(self) -> Tuple[int, int]:
        return self.position
    
    def get_white(self) -> bool:
        return self.white
    
    def get_jumpable(self) -> bool:
        return self.jumpable