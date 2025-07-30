#!/usr/bin/env python3
# rubiks_solver/demo_visual.py

"""
Quick demonstration of the visualization capabilities
"""

import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solver.simple_solver import SimpleCubeSolver, create_solved_cube
from utils.visual import CubeVisualizer
from utils.patterns import get_pattern_algorithm, get_pattern_info

def quick_demo():
    """Quick demonstration of key features"""
    print("🚀 Quick Rubik's Cube Visualization Demo")
    print("=" * 45)
    
    # Initialize components
    solver = SimpleCubeSolver(max_depth=6)
    viz = CubeVisualizer()
    solved_cube = create_solved_cube()
    
    print("1️⃣ Showing solved cube...")
    viz.plot_2d_net(solved_cube, "Solved Rubik's Cube")
    
    print("2️⃣ Applying Sune pattern...")
    sune_moves = get_pattern_algorithm("sune")
    sune_cube = solver.apply_moves(solved_cube, sune_moves)
    viz.plot_2d_net(sune_cube, f"Sune Pattern - {' '.join(sune_moves)}")
    
    print("3️⃣ Comparing solved vs Sune pattern...")
    viz.compare_states(solved_cube, sune_cube, ["Solved State", "Sune Pattern"])
    
    print("4️⃣ Showing 3D visualization...")
    viz.plot_3d_cube(sune_cube, "3D Sune Pattern")
    
    print("5️⃣ Solving the Sune pattern...")
    solution = solver.solve_bfs(sune_cube)
    if solution:
        print(f"✅ Solution found: {' '.join(solution)} ({len(solution)} moves)")
        solved_again = solver.apply_moves(sune_cube, solution)
        viz.plot_2d_net(solved_again, f"Solved! Solution: {' '.join(solution)}")
    else:
        print("❌ No solution found within depth limit")
    
    print("\n🎉 Demo complete! Try the interactive mode:")
    print("   python main.py --interactive")

if __name__ == "__main__":
    quick_demo()
