# rubiks_solver/solver/kociemba.py

# Note: Original kociemba package requires C++ build tools
# Using our simple solver instead

import sys
import os

# Add the project root to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from solver.simple_solver import SimpleCubeSolver, create_solved_cube
except ImportError:
    from .simple_solver import SimpleCubeSolver, create_solved_cube

def solve_kociemba(cube_state):
    """
    Solve a Rubik's cube using our simple BFS solver
    
    Args:
        cube_state: Cube state in our internal format
        
    Returns:
        List of moves to solve the cube, or None if no solution found
    """
    solver = SimpleCubeSolver(max_depth=7)
    solution = solver.solve_bfs(cube_state)
    return solution if solution else []

def solve(cube_string):
    """
    Solve a Rubik's cube from string representation
    
    Args:
        cube_string: String representation of the cube state
        
    Returns:
        String of moves to solve the cube, or None if no solution found
    """
    # For now, demonstrate with a simple example
    # In a real implementation, you'd parse cube_string into our state format
    
    solver = SimpleCubeSolver(max_depth=7)
    
    # Create a simple scrambled state for demonstration
    solved_cube = create_solved_cube()
    scramble = ["R", "U", "R'", "U'"]
    scrambled_cube = solver.apply_moves(solved_cube, scramble)
    
    solution = solver.solve_bfs(scrambled_cube)
    
    if solution:
        return ' '.join(solution)
    return None

def demo():
    """
    Demo function to show the solver in action
    """
    print("Rubik's Cube Solver Demo")
    print("=" * 30)
    
    result = solve("dummy_cube_string")
    if result:
        print(f"Solution: {result}")
    else:
        print("No solution found")

if __name__ == "__main__":
    demo()
