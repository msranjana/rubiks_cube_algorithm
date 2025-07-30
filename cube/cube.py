# rubiks_solver/cube/cube.py

from .moves import MOVE_FUNCS, VALID_MOVES
import copy

class Cube:
    def __init__(self, state=None):
        # Default state: Solved cube, faces listed as [U, R, F, D, L, B]
        self.state = copy.deepcopy(state) if state else [
            ['W']*9,  # Up
            ['R']*9,  # Right
            ['G']*9,  # Front
            ['Y']*9,  # Down
            ['O']*9,  # Left
            ['B']*9   # Back
        ]

    def copy(self):
        return Cube(copy.deepcopy(self.state))

    def apply_move(self, move):
        assert move in VALID_MOVES, f"Invalid move: {move}"
        self.state = MOVE_FUNCS[move](self.state)

    def apply_moves(self, moves):
        for m in moves:
            self.apply_move(m)

    def is_solved(self):
        return all(all(sticker == face[0] for sticker in face) for face in self.state)
