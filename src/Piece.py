from src.Board import Board


class Piece:

    position: (int, int)

    def generate_moves(self, board: Board) -> [(int, int)]:
        pseudo_moves = self.generate_pseudo_legal_moves(board)
        moves = [move for move in pseudo_moves if self.is_legal_move(move, board)]
        return moves

    def generate_pseudo_legal_moves(self, board: Board) -> [(int, int)]:
        pass

    def is_legal_move(self, move: (int, int), board: Board) -> bool:
        pass
        # newBoard: apply move on board
        # board.is_valid
