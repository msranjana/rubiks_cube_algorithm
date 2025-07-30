#!/usr/bin/env python3
# rubiks_solver/main.py

"""
Rubik's Cube Solver
A simple implementation using breadth-first search with visualization
"""

import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from cube.moves import MOVE_FUNCS, VALID_MOVES
from solver.simple_solver import SimpleCubeSolver, create_solved_cube
from utils.visual import CubeVisualizer
from utils.patterns import get_pattern_algorithm, get_pattern_info, list_available_patterns

def main():
    """
    Main function to demonstrate the Rubik's cube solver
    """
    print("🎲 Rubik's Cube Solver with Visualization")
    print("=" * 45)
    
    # Create solver and visualizer
    solver = SimpleCubeSolver(max_depth=6)
    viz = CubeVisualizer()
    
    # Create solved cube
    solved_cube = create_solved_cube()
    print("✅ Created solved cube:")
    print(f"   Up face (White): {solved_cube[0][:3]}")
    print(f"                    {solved_cube[0][3:6]}")
    print(f"                    {solved_cube[0][6:]}")
    
    # Apply a simple scramble
    scramble_moves = ["R", "U", "R'", "U'"]
    print(f"\n🔄 Applying scramble: {' '.join(scramble_moves)}")
    scrambled_cube = solver.apply_moves(solved_cube, scramble_moves)
    
    print("📦 Scrambled cube:")
    print(f"   Up face: {scrambled_cube[0][:3]}")
    print(f"            {scrambled_cube[0][3:6]}")
    print(f"            {scrambled_cube[0][6:]}")
    
    # Show visualization of scrambled state
    print("\n🎨 Showing visual comparison...")
    viz.compare_states(solved_cube, scrambled_cube, 
                      ["Solved State", f"Scrambled - {' '.join(scramble_moves)}"])
    
    # Solve the cube
    print("\n🧠 Solving cube...")
    solution = solver.solve_bfs(scrambled_cube)
    
    if solution:
        print(f"✅ Solution found: {' '.join(solution)}")
        print(f"   Moves required: {len(solution)}")
        
        # Verify solution
        solved_again = solver.apply_moves(scrambled_cube, solution)
        if solver.is_solved(solved_again):
            print("✅ Solution verified successfully!")
        else:
            print("❌ Solution verification failed!")
            
        # Show the solved cube
        print("\n🎯 Final cube state:")
        print(f"   Up face: {solved_again[0][:3]}")
        print(f"            {solved_again[0][3:6]}")
        print(f"            {solved_again[0][6:]}")
        
        # Show final visualization
        print("\n🎨 Showing final result...")
        viz.plot_2d_net(solved_again, f"Solved! Solution: {' '.join(solution)}")
            
    else:
        print("❌ No solution found within depth limit")
        print("   Try increasing max_depth or use a different scramble")

def interactive_mode():
    """
    Interactive mode for testing different scrambles with visualization
    """
    solver = SimpleCubeSolver(max_depth=6)
    viz = CubeVisualizer()
    solved_cube = create_solved_cube()
    
    print("\n🎮 Interactive Mode with Visualization")
    print("Available moves:", ' '.join(VALID_MOVES))
    print("Commands:")
    print("  - Enter moves separated by spaces")
    print("  - 'show' - display current scrambled state")
    print("  - 'compare' - compare with solved state")
    print("  - '3d' - show 3D visualization")
    print("  - 'pattern <name>' - apply a pattern")
    print("  - 'patterns' - list available patterns")
    print("  - 'reset' - return to solved state")
    print("  - 'quit' - exit")
    
    current_scramble = []
    
    while True:
        try:
            user_input = input(f"\n[{len(current_scramble)} moves] > ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            elif user_input.lower() == 'reset':
                current_scramble = []
                print("🔄 Reset to solved state")
                continue
            elif user_input.lower() == 'patterns':
                patterns = list_available_patterns()
                print("🎨 Available patterns:")
                for pattern in patterns:
                    info = get_pattern_info(pattern)
                    if info:
                        print(f"  • {pattern}: {info['description']}")
                continue
            elif user_input.lower().startswith('pattern '):
                pattern_name = user_input[8:].strip()
                pattern_moves = get_pattern_algorithm(pattern_name)
                if pattern_moves:
                    info = get_pattern_info(pattern_name)
                    current_scramble = pattern_moves.copy()
                    scrambled_cube = solver.apply_moves(solved_cube, current_scramble)
                    print(f"🎨 Applied pattern: {info['name']}")
                    print(f"   Algorithm: {' '.join(pattern_moves)}")
                    print(f"   Description: {info['description']}")
                    viz.plot_2d_net(scrambled_cube, f"Pattern: {info['name']}")
                else:
                    print(f"❌ Pattern '{pattern_name}' not found")
                continue
            elif user_input.lower() == 'show':
                if current_scramble:
                    scrambled_cube = solver.apply_moves(solved_cube, current_scramble)
                    viz.plot_2d_net(scrambled_cube, f"Current State - {' '.join(current_scramble)}")
                else:
                    viz.plot_2d_net(solved_cube, "Solved State")
                continue
            elif user_input.lower() == 'compare':
                if current_scramble:
                    scrambled_cube = solver.apply_moves(solved_cube, current_scramble)
                    viz.compare_states(solved_cube, scrambled_cube, 
                                     ["Solved", f"Scrambled - {' '.join(current_scramble)}"])
                else:
                    print("No scramble applied yet")
                continue
            elif user_input.lower() == '3d':
                if current_scramble:
                    scrambled_cube = solver.apply_moves(solved_cube, current_scramble)
                    viz.plot_3d_cube(scrambled_cube, f"3D View - {' '.join(current_scramble)}")
                else:
                    viz.plot_3d_cube(solved_cube, "3D Solved Cube")
                continue
                
            moves = user_input.split()
            if not moves:
                continue
                
            # Validate moves
            invalid_moves = [move for move in moves if move not in VALID_MOVES]
            if invalid_moves:
                print(f"❌ Invalid moves: {invalid_moves}")
                continue
            
            # Apply scramble
            current_scramble.extend(moves)
            scrambled_cube = solver.apply_moves(solved_cube, current_scramble)
            print(f"Applied moves: {' '.join(moves)}")
            print(f"Total scramble: {' '.join(current_scramble)}")
            
            # Auto-show visualization for new scramble
            viz.plot_2d_net(scrambled_cube, f"Current State - {' '.join(current_scramble)}")
            
            # Try to solve
            solution = solver.solve_bfs(scrambled_cube)
            if solution:
                print(f"✅ Solution: {' '.join(solution)} ({len(solution)} moves)")
            else:
                print("❌ No solution found within depth limit")
                
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("👋 Goodbye!")

def visualization_demo():
    """
    Run a comprehensive visualization demo
    """
    print("\n🎨 Comprehensive Visualization Demo")
    print("=" * 40)
    
    solver = SimpleCubeSolver(max_depth=6)
    viz = CubeVisualizer()
    
    # Create different cube states
    solved_cube = create_solved_cube()
    
    # Various scrambles to show different visualizations
    scrambles = [
        (["R", "U", "R'", "U'"], "Simple T-Perm Pattern"),
        (["R", "U", "R'", "U'", "R", "U2", "R'"], "Extended Pattern"),
        (["F", "R", "U'", "R'", "U'", "R", "U", "R'", "F'"], "OLL Pattern"),
    ]
    
    # Show solved state first
    print("📊 1. Solved Cube")
    viz.plot_2d_net(solved_cube, "Solved Rubik's Cube")
    
    # Show each scramble
    for i, (moves, description) in enumerate(scrambles, 2):
        scrambled = solver.apply_moves(solved_cube, moves)
        print(f"📊 {i}. {description}")
        viz.plot_2d_net(scrambled, f"{description} - {' '.join(moves)}")
    
    # Show comparison
    print("📊 5. State Comparison")
    scrambled1 = solver.apply_moves(solved_cube, scrambles[0][0])
    scrambled2 = solver.apply_moves(solved_cube, scrambles[1][0])
    viz.compare_states(scrambled1, scrambled2, 
                      [scrambles[0][1], scrambles[1][1]])
    
    # Show 3D if available
    try:
        print("📊 6. 3D Visualization")
        viz.plot_3d_cube(solved_cube, "3D Solved Cube")
        scrambled_3d = solver.apply_moves(solved_cube, scrambles[0][0])
        viz.plot_3d_cube(scrambled_3d, f"3D {scrambles[0][1]}")
    except Exception as e:
        print(f"3D visualization not available: {e}")

def pattern_demo():
    """
    Demo showcasing various cube patterns
    """
    print("\n🎨 Cube Pattern Visualization Demo")
    print("=" * 40)
    
    solver = SimpleCubeSolver()
    viz = CubeVisualizer()
    solved_cube = create_solved_cube()
    
    # Get available patterns
    patterns = list_available_patterns()[:6]  # Show first 6 patterns
    
    print(f"📊 Showing {len(patterns)} patterns...")
    
    for i, pattern_name in enumerate(patterns, 1):
        pattern_info = get_pattern_info(pattern_name)
        if pattern_info and pattern_info["algorithm"]:
            pattern_cube = solver.apply_moves(solved_cube, pattern_info["algorithm"])
            print(f"📊 {i}. {pattern_info['name']}")
            viz.plot_2d_net(pattern_cube, 
                           f"{pattern_info['name']} - {' '.join(pattern_info['algorithm'])}")
        else:
            print(f"📊 {i}. {pattern_name} (Solved state)")
            viz.plot_2d_net(solved_cube, f"{pattern_name}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--interactive":
            interactive_mode()
        elif sys.argv[1] == "--demo":
            visualization_demo()
        elif sys.argv[1] == "--patterns":
            pattern_demo()
        elif sys.argv[1] == "--visual-demo":
            # Run the visual module demo
            from utils.visual import demo_visualization
            demo_visualization()
        else:
            print("Usage:")
            print("  python main.py                 # Basic demo")
            print("  python main.py --interactive   # Interactive mode")
            print("  python main.py --demo          # Visualization demo")
            print("  python main.py --patterns      # Pattern showcase")
            print("  python main.py --visual-demo   # Visual module demo")
    else:
        main()
