from tetrakis import Tetrakis, generate_alpha, generate_alpha_range, cell
import player

from itertools import product


class NoWinnerException(Exception):
    pass


class Board(object):
    def __init__(self, height, width):
        self.width = width
        self.height = height

        self.white_pieces = []
        self.black_pieces = []

        self.__turn = player.WHITE
        self.__winner = None

        self.board = Tetrakis(height, width)
        dense_row_height = (height - 1) >> 1
        sparse_row_width = (width - 1) >> 1

        # Populate the board
        for row, col in product(range(dense_row_height), generate_alpha(width)):
            self.board.set_contents(cell(row, col), player.BLACK)
        for row, col in product(range(dense_row_height + 1, height), generate_alpha(width)):
            self.board.set_contents(cell(row, col), player.WHITE)
        for row, col in product([dense_row_height], generate_alpha_range('a', width, 2)):
            if cell(row, col) == cell(dense_row_height, chr(ord('a') + sparse_row_width)):
                self.board.set_contents(cell(row, col), player.EMPTY)
            else:
                self.board.set_contents(cell(row, col), player.BLACK)
        for row, col in product([dense_row_height], generate_alpha_range('b', width, 2)):
            self.board.set_contents(cell(row, col), player.WHITE)

    def next_states(self) -> '[Board]':
        boards = []
        for piece in self.pieces(self.turn):
            boards += piece.moves()
        return boards

    def next_state(self, piece, move_pos) -> 'Board':
        self.board.set_content(piece.pos, player.EMPTY)
        self.board.set_content(move_pos, piece.player)

        #if self.board.is_strong_intersection(piece.pos):
        #	for i in range(

    def is_gameover(self) -> 'bool':
        if len(self.white_pieces) == 0:
            self.winner = player.BLACK
            return True
        elif len(self.black_pieces) == 0:
            self.winner = player.WHITE
            return True
        return False

    def pieces(self, turn):
        return self.white_pieces if turn == player.WHITE else self.black_pieces

    def alternate_turn(self):
        self.turn = player.get_opposite(self.turn)

    def __str__(self):
        buffer = ""
        content_buffer = ""
        counter = 1
        for pos, contents in sorted(self.board.nodes):
            if counter % self.height == 0:
                content_buffer += " " + str(contents) + '\n'
                buffer += content_buffer
                content_buffer = ""
            elif counter % self.height == 1:
                content_buffer += str(contents)
            else:
                content_buffer += " " + str(contents)
            counter += 1
        return buffer

    def print_board(self):
        print(self)

    @property
    def turn(self):
        return self.__turn

    @turn.setter
    def turn(self, value):
        self.__turn = value

    @property
    def winner(self):
        if self.__winner is not None:
            raise NoWinnerException()
        return self.__winner

    @winner.setter
    def winner(self, value):
        self.__winner = value
