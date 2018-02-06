from sys import argv
from math import sqrt, modf
from enum import Enum
from collections import namedtuple

Loc = namedtuple('Loc', 'row col')

Move = Enum('Move', 'Up Down Left Right')

class Board:
    EMPTY_TILE = 0
    POSSIBLE_MOVE = {
        Move.Up: lambda b: b.empty_loc.row > 0,
        Move.Down: lambda b: b.empty_loc.row < b.dim - 1,
        Move.Left: lambda b: b.empty_loc.col > 0,
        Move.Right: lambda b: b.empty_loc.col < b.dim - 1
        }
    def __init__(self, board_str):
        board_arr = list(map(lambda s: int(s), board_str.split(',')))
        self.dim = self.init_dim(board_arr)
        self.board = self.init_board(board_arr)
        self.solution = self.init_solution()
        self.empty_loc = self.init_empty_loc()
    def init_dim(self, board_arr):
        dims = modf(sqrt(len(board_arr)))
        assert dims[0] == 0.0, 'board is not square'
        return int(dims[1])
    def init_board(self, board_arr):
        board = []
        start = 0
        for end in range(self.dim, self.dim**2 + 1, self.dim):
            board.append(board_arr[start:end])
            start = end
        return board
    def init_solution(self):
        n = self.dim
        return [[j for j in range(n*i, n*(i+1))] for i in range(0,n)]
    def init_empty_loc(self):
        for row in range(0, self.dim):
            for col in range(0, self.dim):
                if self.board[row][col] == Board.EMPTY_TILE:
                    return Loc(row,col)
        raise Exception('blank tile not present')
    def can_move(self, move):
        return Board.POSSIBLE_MOVE[move](self)

class search_alg:
    pass

def bfs():
    return 'bfs'
def dfs():
    return 'dfs'
def ast():
    return 'ast'

ALG_DICT = {'bfs':bfs, 'dfs':dfs, 'ast':ast}

def main(alg_str, board_str):
    a =  ALG_DICT[alg_str]()
    b = Board(board_str)
    print(a)
    print(b.empty_loc)
    print(Move.Down.name)

if __name__ == '__main__':
    main(argv[1], argv[2])
