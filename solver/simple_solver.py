# rubiks_solver/solver/simple_solver.py

from collections import deque
import copy
import sys
import os

# Add the project root to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from cube.moves import MOVE_FUNCS, VALID_MOVES
except ImportError:
    # If running as script, try relative import
    from ..cube.moves import MOVE_FUNCS, VALID_MOVES

class SimpleCubeSolver:
    def __init__(self, max_depth=7):
        """
        Simple BFS solver for Rubik's cube
        max_depth: Maximum search depth (keep low due to exponential growth)
        """
        self.max_depth = max_depth
        
    def is_solved(self, state):
        """
        Check if the cube is in solved state
        A solved cube has all faces with the same color
        """
        for face in state:
            if not all(sticker == face[0] for sticker in face):
                return False
        return True
    
    def get_scrambled_moves(self, num_moves=5):
        """
        Generate a random scramble sequence
        """
        import random
        return [random.choice(VALID_MOVES) for _ in range(num_moves)]
    
    def apply_moves(self, state, moves):
        """
        Apply a sequence of moves to a cube state
        """
        current_state = copy.deepcopy(state)
        for move in moves:
            if move in MOVE_FUNCS:
                current_state = MOVE_FUNCS[move](current_state)
        return current_state
    
    def solve_bfs(self, initial_state):
        """
        Solve using breadth-first search
        Returns the sequence of moves to solve the cube
        """
        if self.is_solved(initial_state):
            return []
        
        # Queue: (state, moves_to_reach_state)
        queue = deque([(initial_state, [])])
        visited = set()
        
        # Convert state to string for hashing
        def state_to_string(state):
            return str(state)
        
        visited.add(state_to_string(initial_state))
        
        while queue:
            current_state, moves = queue.popleft()
            
            if len(moves) >= self.max_depth:
                continue
                
            # Try each possible move
            for move in VALID_MOVES:
                new_state = MOVE_FUNCS[move](current_state)
                new_moves = moves + [move]
                
                if self.is_solved(new_state):
                    return new_moves
                
                state_str = state_to_string(new_state)
                if state_str not in visited:
                    visited.add(state_str)
                    queue.append((new_state, new_moves))
        
        return None  # No solution found within max_depth

def create_solved_cube():
    """
    Create a solved cube state
    State format: [Up, Right, Front, Down, Left, Back]
    Each face is a list of 9 stickers (0-8)
    Colors: 0=White, 1=Red, 2=Green, 3=Yellow, 4=Orange, 5=Blue
    """
    return [
        [0] * 9,  # Up (White)
        [1] * 9,  # Right (Red)  
        [2] * 9,  # Front (Green)
        [3] * 9,  # Down (Yellow)
        [4] * 9,  # Left (Orange)
        [5] * 9   # Back (Blue)
    ]

def demo_solver():
    """
    Demonstrate the solver with a simple scramble
    """
    solver = SimpleCubeSolver(max_depth=6)
    
    # Create solved cube
    solved_cube = create_solved_cube()
    print("Solved cube:")
    print(solved_cube)
    
    # Apply a simple scramble
    scramble_moves = ["R", "U", "R'", "U'"]
    scrambled_cube = solver.apply_moves(solved_cube, scramble_moves)
    
    print(f"\nScramble applied: {' '.join(scramble_moves)}")
    print("Scrambled cube:")
    print(scrambled_cube)
    
    # Solve the cube
    print("\nSolving...")
    solution = solver.solve_bfs(scrambled_cube)
    
    if solution:
        print(f"Solution found: {' '.join(solution)}")
        
        # Verify solution
        solved_again = solver.apply_moves(scrambled_cube, solution)
        if solver.is_solved(solved_again):
            print("✓ Solution verified!")
        else:
            print("✗ Solution verification failed!")
    else:
        print("No solution found within depth limit")

if __name__ == "__main__":
    demo_solver()
