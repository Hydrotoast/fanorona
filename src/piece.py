import player
import copy


class Piece(object):
    def __init__(self, board, player, pos):
        self.board = board
        self.player = player
        self.pos = pos

    def moves(self) -> '[Board]':
        boards = []

        # Can capture multiple times
        if self.can_capture(self.board):
            self.capturing(self, self.pos, self.board, boards)
            return boards

        for pos in self.board.edges(self.pos):
            clone = copy.deepcopy(self.board)
            clone.next_state(self, pos)

            # Single move
            boards.append(clone)
        return boards

    def capturing(self, piece, pos, board, boards):
        if not self.can_capture(board):
            return
        for further_pos in board.ajacencies(pos):
            clone = copy.deepcopy(clone)
            piece_clone = copy.deepcopy(piece)
            clone.next_state(piece_clone, further_pos)
            boards.append(clone)
            self.capturing(piece_clone, further_pos, clone, boards)

    def can_capture(self, board) -> 'Bool':
        for pos in self.board.adjacencies(self.pos):
            for next_pos in self.board.adjacencies(pos):
                if self.board[pos] == self.opponent_piece():
                    return True
        return False

    def opponent_piece(self) -> 'Player':
        return player.get_opposite(self.player)
