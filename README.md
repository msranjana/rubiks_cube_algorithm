# Rubik's Cube Solver with Visualization

A Python implementation of a Rubik's cube solver using breadth-first search with comprehensive matplotlib visualization capabilities.

## Features

- ✅ Complete move implementation (U, D, R, L, F, B and their inverses)
- ✅ Breadth-first search solver for small scrambles
- ✅ **2D cube visualization** with unfolded net display
- ✅ **3D cube visualization** with rotating 3D cube
- ✅ **Interactive mode** with real-time visualization
- ✅ **Pattern generator** with classic cube patterns
- ✅ **State comparison** visualization
- ✅ Solution verification
- ✅ No C++ dependencies required

## Installation

1. Navigate to the project directory:
```bash
cd rubiks_solver
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

The required packages include:
- `numpy` - For numerical operations
- `matplotlib` - For visualization
- `colorama` - For colored terminal output

## Usage

### Basic Demo with Visualization
```bash
python main.py
```
Shows a complete solving process with before/after visualizations.

### Interactive Mode
```bash
python main.py --interactive
```

In interactive mode, you can:
- Enter custom scrambles using standard Rubik's cube notation
- Use `show` to display current cube state
- Use `compare` to compare with solved state
- Use `3d` to show 3D visualization
- Use `pattern <name>` to apply predefined patterns
- Use `patterns` to list available patterns
- Use `reset` to return to solved state

Example interactive session:
```
[0 moves] > R U R' U'
Applied moves: R U R' U'
Total scramble: R U R' U'
✅ Solution: U R U' R' (4 moves)

[4 moves] > pattern sune
🎨 Applied pattern: Sune Pattern
   Algorithm: R U R' U R U2 R'
   Description: Classic Sune algorithm pattern

[7 moves] > 3d
# Shows 3D visualization

[7 moves] > reset
🔄 Reset to solved state
```

### Visualization Demos
```bash
python main.py --demo          # Comprehensive visualization demo
python main.py --patterns      # Pattern showcase
python main.py --visual-demo   # Visual module demo
```

## Visualization Features

### 2D Net Visualization
- **Unfolded cube display**: Shows all 6 faces in a cross pattern
- **Color-coded stickers**: Each face has its distinct color
- **Face labels**: Clear identification of each face
- **Grid lines**: Clean separation between faces and stickers

### 3D Cube Visualization  
- **Rotating 3D cube**: Interactive 3D representation
- **Proper face orientations**: Accurate spatial relationships
- **Customizable viewing angles**: Adjustable perspective

### State Comparison
- **Side-by-side comparison**: Compare two cube states
- **Before/after solving**: Visual verification of solutions
- **Pattern comparison**: Compare different algorithms

### Pattern Library
Built-in patterns include:
- **Sune/Anti-Sune**: Classic OLL algorithms
- **T-Pattern**: Simple beginner pattern  
- **Cross Pattern**: Creates cross formations
- **Corner/Edge patterns**: Targeted piece manipulation
- **And more**: Various speedcubing patterns

## Project Structure

```
rubiks_solver/
├── main.py              # Main entry point with visualization
├── requirements.txt     # Python dependencies (updated)
├── README.md           # This file
├── cube/
│   ├── __init__.py
│   ├── cube.py         # Cube representation (placeholder)
│   └── moves.py        # Move implementations
├── solver/
│   ├── __init__.py
│   ├── kociemba.py     # Solver interface
│   ├── simple_solver.py # BFS solver implementation
│   └── search.py       # Search algorithms (placeholder)
└── utils/
    ├── __init__.py
    ├── parser.py       # Input parsing (placeholder)
    ├── patterns.py     # Pattern algorithms and generator
    └── visual.py       # Comprehensive visualization module
```

## Technical Details

### Cube Representation
The cube state is represented as a list of 6 faces, each face containing 9 stickers:
- Face 0: Up (White) - `#FFFFFF`
- Face 1: Right (Red) - `#FF0000`
- Face 2: Front (Green) - `#00FF00`
- Face 3: Down (Yellow) - `#FFFF00`
- Face 4: Left (Orange) - `#FFA500`
- Face 5: Back (Blue) - `#0000FF`

### Visualization Architecture
The `CubeVisualizer` class provides:
- `plot_2d_net()` - 2D unfolded cube display
- `plot_3d_cube()` - 3D cube representation
- `compare_states()` - Side-by-side state comparison
- `animate_solve()` - Animation framework (future)

### Pattern System
The pattern system includes:
- **Simple patterns**: Work with basic moves only
- **Complex patterns**: Include middle layer moves (for reference)
- **Pattern info**: Name, algorithm, and description
- **Random pattern generation**: For testing and fun

### Solver Algorithm
The current implementation uses breadth-first search (BFS) with a configurable maximum depth. This approach:
- Guarantees optimal solutions (minimum number of moves)
- Works well for scrambles up to ~7 moves
- Has exponential time complexity, so depth is limited

### Visualization Examples

**2D Net Layout:**
```
        [U]
    [L] [F] [R] [B]
        [D]
```

**Available Commands:**
- Basic solving: `python main.py`
- Interactive: `python main.py --interactive`
- Pattern demo: `python main.py --patterns`
- Full demo: `python main.py --demo`

## Advanced Usage

### Custom Patterns
You can create custom patterns by modifying `utils/patterns.py`:

```python
CUSTOM_PATTERN = {
    "name": "My Pattern",
    "algorithm": ["R", "U", "R'", "U'"],
    "description": "My custom pattern description"
}
```

### Saving Visualizations
All visualization functions support saving:

```python
viz = CubeVisualizer()
viz.plot_2d_net(cube_state, "My Cube", save_path="my_cube.png")
```

### Color Customization
Modify the `COLORS` dictionary in `utils/visual.py` to customize face colors.

## Limitations
- Maximum solving depth is limited to prevent excessive computation time
- Only solves relatively simple scrambles efficiently
- 3D visualization is basic (shows face colors, not individual stickers)
- Animation features are planned for future implementation

## Future Enhancements

- [ ] **Step-by-step animation** of solving process
- [ ] **Individual sticker rendering** in 3D view
- [ ] **Webcam cube detection** for real-world solving
- [ ] **Advanced algorithms** (Kociemba's two-phase)
- [ ] **Web interface** with interactive 3D cube
- [ ] **Move history** and undo functionality
- [ ] **Cube timer** integration
- [ ] **Export/import** cube states

## Performance Notes

- **2D visualization**: Very fast, suitable for real-time updates
- **3D visualization**: Moderate performance, good for demonstrations
- **Pattern generation**: Instant for simple patterns
- **BFS solving**: Limited to ~7 moves for reasonable performance

## Note on Kociemba Package

The original plan was to use the `kociemba` Python package, but it requires Microsoft Visual C++ 14.0 or greater for compilation. To avoid build tool dependencies, this implementation provides a simple alternative solver with comprehensive visualization that works without any compilation requirements.

## Dependencies

All dependencies are pure Python packages:
- `numpy>=1.20.0` - Numerical operations
- `matplotlib>=3.3.0` - Plotting and visualization
- `colorama>=0.4.4` - Terminal colors

## Contributing

Feel free to contribute improvements, especially:
- Enhanced 3D visualization with individual stickers
- Animation system for move sequences  
- Additional cube patterns and algorithms
- Performance optimizations for larger search depths
- Web interface development
- Mobile app integration

## Examples

### Quick Start
```bash
# Basic demo with visualization
python main.py

# Try interactive mode
python main.py --interactive
> pattern sune
> show
> 3d
> reset
> R U R' U'
> compare
```

### Pattern Showcase
```bash
# See all available patterns
python main.py --patterns
```

This will show visual representations of various cube patterns including Sune, Anti-Sune, T-patterns, and more.

## License

This project is open source and available under the MIT License.
