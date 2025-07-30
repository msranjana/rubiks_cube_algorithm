#!/usr/bin/env python3
# rubiks_solver/utils/patterns.py

"""
Rubik's Cube Pattern Generator
Contains algorithms for creating interesting cube patterns
"""

# Common Rubik's cube patterns with their algorithms
PATTERNS = {
    "solved": {
        "name": "Solved Cube",
        "algorithm": [],
        "description": "The solved state of the Rubik's cube"
    },
    "checkerboard": {
        "name": "Checkerboard Pattern",
        "algorithm": ["M2", "E2", "S2"],
        "description": "Creates a checkerboard pattern on all faces"
    },
    "cross": {
        "name": "Cross Pattern",
        "algorithm": ["F", "R", "U'", "R'", "U'", "R", "U", "R'", "F'"],
        "description": "Creates cross patterns on opposite faces"
    },
    "t_perm": {
        "name": "T-Permutation",
        "algorithm": ["R", "U", "R'", "U'", "R'", "F", "R2", "U'", "R'", "U'", "R", "U", "R'", "F'"],
        "description": "T-Permutation algorithm pattern"
    },
    "y_perm": {
        "name": "Y-Permutation", 
        "algorithm": ["R", "U'", "R'", "U'", "R", "U", "R'", "F'", "R", "U", "R'", "U'", "R'", "F", "R"],
        "description": "Y-Permutation algorithm pattern"
    },
    "sune": {
        "name": "Sune Pattern",
        "algorithm": ["R", "U", "R'", "U", "R", "U2", "R'"],
        "description": "Classic Sune algorithm pattern"
    },
    "antisune": {
        "name": "Anti-Sune Pattern",
        "algorithm": ["R'", "U'", "R", "U'", "R'", "U2", "R"],
        "description": "Anti-Sune algorithm pattern"
    },
    "h_perm": {
        "name": "H-Permutation",
        "algorithm": ["M2", "U", "M2", "U2", "M2", "U", "M2"],
        "description": "H-Permutation algorithm pattern"
    },
    "j_perm": {
        "name": "J-Permutation",
        "algorithm": ["R", "U", "R'", "F'", "R", "U", "R'", "U'", "R'", "F", "R2", "U'", "R'"],
        "description": "J-Permutation algorithm pattern"
    },
    "cube_in_cube": {
        "name": "Cube in Cube",
        "algorithm": ["F", "L", "F", "U'", "R", "U", "F2", "L2", "U'", "L'", "B", "D'", "B'", "L2", "U"],
        "description": "Creates a cube pattern within the cube"
    },
    "flower": {
        "name": "Flower Pattern",
        "algorithm": ["R", "U", "R'", "U", "R", "U2", "R'", "F", "R", "U", "R'", "U'", "F'"],
        "description": "Creates flower-like patterns"
    },
    "dots": {
        "name": "Six Dots",
        "algorithm": ["F", "R'", "F'", "R", "U", "R", "U'", "R'"],
        "description": "Creates dot patterns on faces"
    },
    "superflip": {
        "name": "Superflip",
        "algorithm": ["R", "L", "U2", "F", "U'", "D", "R2", "L'", "D'", "B2", "R'", "D", "R2", "F", "L", "B2", "U2", "F2"],
        "description": "All edges flipped, corners solved - requires 20 moves to solve"
    }
}

# Simplified patterns that work with our basic moves (no middle layer moves)
SIMPLE_PATTERNS = {
    "solved": PATTERNS["solved"],
    "simple_cross": {
        "name": "Simple Cross",
        "algorithm": ["F", "R", "U'", "R'", "U'", "R", "U", "R'", "F'"],
        "description": "Creates a simple cross pattern"
    },
    "t_pattern": {
        "name": "T-Pattern",
        "algorithm": ["R", "U", "R'", "U'"],
        "description": "Simple T-pattern (beginner friendly)"
    },
    "sune": PATTERNS["sune"],
    "antisune": PATTERNS["antisune"],
    "double_sune": {
        "name": "Double Sune",
        "algorithm": ["R", "U", "R'", "U", "R", "U2", "R'", "R", "U", "R'", "U", "R", "U2", "R'"],
        "description": "Double Sune pattern"
    },
    "corners": {
        "name": "Corner Pattern",
        "algorithm": ["R", "U2", "R'", "U'", "R", "U'", "R'"],
        "description": "Affects mainly corners"
    },
    "edges": {
        "name": "Edge Pattern", 
        "algorithm": ["F", "U", "R", "U'", "R'", "F'"],
        "description": "Affects mainly edges"
    },
    "zigzag": {
        "name": "Zigzag Pattern",
        "algorithm": ["R", "U", "B'", "R", "B", "R'", "U'", "R'"],
        "description": "Creates zigzag patterns"
    },
    "spiral": {
        "name": "Spiral Pattern",
        "algorithm": ["R", "U", "R'", "F", "R", "F'", "U'", "R", "U", "R'", "U'"],
        "description": "Creates spiral-like patterns"
    }
}

def get_pattern_algorithm(pattern_name):
    """
    Get the algorithm for a specific pattern
    
    Args:
        pattern_name: Name of the pattern
        
    Returns:
        List of moves for the pattern, or None if pattern doesn't exist
    """
    if pattern_name in SIMPLE_PATTERNS:
        return SIMPLE_PATTERNS[pattern_name]["algorithm"]
    elif pattern_name in PATTERNS:
        return PATTERNS[pattern_name]["algorithm"]
    return None

def get_pattern_info(pattern_name):
    """
    Get information about a specific pattern
    
    Args:
        pattern_name: Name of the pattern
        
    Returns:
        Dictionary with pattern information, or None if pattern doesn't exist
    """
    if pattern_name in SIMPLE_PATTERNS:
        return SIMPLE_PATTERNS[pattern_name]
    elif pattern_name in PATTERNS:
        return PATTERNS[pattern_name]
    return None

def list_available_patterns():
    """
    List all available patterns
    
    Returns:
        List of pattern names
    """
    return list(SIMPLE_PATTERNS.keys())

def list_all_patterns():
    """
    List all patterns including complex ones
    
    Returns:
        List of all pattern names
    """
    return list(PATTERNS.keys())

def get_random_pattern():
    """
    Get a random pattern from simple patterns
    
    Returns:
        Random pattern name and its info
    """
    import random
    pattern_name = random.choice(list(SIMPLE_PATTERNS.keys()))
    return pattern_name, SIMPLE_PATTERNS[pattern_name]

def demo_patterns():
    """
    Demo function to show available patterns
    """
    print("🎨 Available Cube Patterns")
    print("=" * 30)
    
    print("\n📋 Simple Patterns (work with basic moves):")
    for name, info in SIMPLE_PATTERNS.items():
        moves = " ".join(info["algorithm"]) if info["algorithm"] else "None"
        print(f"  • {info['name']}")
        print(f"    Algorithm: {moves}")
        print(f"    Description: {info['description']}")
        print()
    
    print(f"\n📊 Total simple patterns: {len(SIMPLE_PATTERNS)}")
    print(f"📊 Total all patterns: {len(PATTERNS)}")

if __name__ == "__main__":
    demo_patterns()
