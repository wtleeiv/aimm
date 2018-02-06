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
        Move.Down: lambda b: b.empty_loc.row < b.board_dim - 1,
        Move.Left: lambda b: b.empty_loc.col > 0,
        Move.Right: lambda b: b.empty_loc.col < b.board_dim - 1
        }
    def __init__(self, board_str):
        board_arr = list(map(lambda s: int(s), board_str.split(',')))
        self.board_dim = self.init_board_dim(board_arr)
        self.layout = self.init_layout(board_arr)
        self.solution = self.init_solution()
        self.empty_loc = self.init_empty_loc()
    def init_board_dim(self, board_arr):
        dims = modf(sqrt(len(board_arr)))
        assert dims[0] == 0.0, 'board is not square'
        return int(dims[1])
    def init_layout(self, board_arr):
        layout = []
        start = 0
        for end in range(self.board_dim, self.board_dim**2 + 1, self.board_dim):
            layout.append(board_arr[start:end])
            start = end
        return layout
    def init_solution(self):
        n = self.board_dim
        return [[j for j in range(n*i, n*(i+1))] for i in range(0,n)]
    def init_empty_loc(self):
        for row in range(0, self.board_dim):
            for col in range(0, self.board_dim):
                if self.layout[row][col] == Board.EMPTY_TILE:
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
