#!/usr/bin/env python3
# rubiks_solver/utils/visual.py

"""
Rubik's Cube Visualization using matplotlib
Provides 2D and 3D visualization of cube states
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sys
import os

# Add the project root to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Color mapping for cube faces
COLORS = {
    0: '#FFFFFF',  # White (Up)
    1: '#FF0000',  # Red (Right)
    2: '#00FF00',  # Green (Front)
    3: '#FFFF00',  # Yellow (Down)
    4: '#FFA500',  # Orange (Left)
    5: '#0000FF'   # Blue (Back)
}

FACE_NAMES = {
    0: 'Up (White)',
    1: 'Right (Red)',
    2: 'Front (Green)',
    3: 'Down (Yellow)',
    4: 'Left (Orange)',
    5: 'Back (Blue)'
}

class CubeVisualizer:
    def __init__(self):
        self.fig = None
        self.ax = None
    
    def plot_2d_net(self, cube_state, title="Rubik's Cube State", save_path=None):
        """
        Plot the cube as a 2D net (unfolded cube)
        
        Args:
            cube_state: List of 6 faces, each face is a list of 9 stickers
            title: Title for the plot
            save_path: Optional path to save the figure
        """
        self.fig, self.ax = plt.subplots(1, 1, figsize=(12, 9))
        self.ax.set_xlim(0, 12)
        self.ax.set_ylim(0, 9)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        
        # Define positions for each face in the net
        # Layout:    [U]
        #        [L][F][R][B]
        #            [D]
        face_positions = {
            0: (3, 6),  # Up
            1: (6, 3),  # Right
            2: (3, 3),  # Front
            3: (3, 0),  # Down
            4: (0, 3),  # Left
            5: (9, 3)   # Back
        }
        
        # Draw each face
        for face_idx, (start_x, start_y) in face_positions.items():
            self._draw_face(cube_state[face_idx], start_x, start_y, face_idx)
        
        # Add title and face labels
        self.ax.text(6, 8.5, title, ha='center', va='center', fontsize=16, fontweight='bold')
        
        # Add face labels
        for face_idx, (start_x, start_y) in face_positions.items():
            face_name = FACE_NAMES[face_idx]
            self.ax.text(start_x + 1.5, start_y + 3.3, face_name, 
                        ha='center', va='center', fontsize=10, fontweight='bold')
        
        # Add grid lines for clarity
        self._add_grid_lines(face_positions)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()
        return self.fig
    
    def _draw_face(self, face, start_x, start_y, face_idx):
        """Draw a single 3x3 face"""
        for i in range(3):
            for j in range(3):
                sticker_idx = i * 3 + j
                color = COLORS[face[sticker_idx]]
                
                x = start_x + j
                y = start_y + (2 - i)  # Flip Y coordinate
                
                # Draw the sticker
                rect = patches.Rectangle((x, y), 1, 1, 
                                       linewidth=2, 
                                       edgecolor='black', 
                                       facecolor=color)
                self.ax.add_patch(rect)
                
                # Add sticker index for debugging (optional)
                # self.ax.text(x + 0.5, y + 0.5, str(sticker_idx), 
                #            ha='center', va='center', fontsize=8)
    
    def _add_grid_lines(self, face_positions):
        """Add grid lines around each face"""
        for face_idx, (start_x, start_y) in face_positions.items():
            # Draw face border
            border = patches.Rectangle((start_x, start_y), 3, 3, 
                                     linewidth=3, 
                                     edgecolor='black', 
                                     facecolor='none')
            self.ax.add_patch(border)
    
    def plot_3d_cube(self, cube_state, title="3D Rubik's Cube", save_path=None):
        """
        Plot the cube in 3D
        
        Args:
            cube_state: List of 6 faces, each face is a list of 9 stickers
            title: Title for the plot
            save_path: Optional path to save the figure
        """
        self.fig = plt.figure(figsize=(10, 8))
        self.ax = self.fig.add_subplot(111, projection='3d')
        
        # Define the 6 faces of the cube with their positions and orientations
        self._draw_3d_cube_faces(cube_state)
        
        # Set equal aspect ratio and remove axes
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        
        # Set viewing angle
        self.ax.view_init(elev=20, azim=45)
        
        # Set limits
        self.ax.set_xlim([0, 3])
        self.ax.set_ylim([0, 3])
        self.ax.set_zlim([0, 3])
        
        plt.title(title, fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()
        return self.fig
    
    def _draw_3d_cube_faces(self, cube_state):
        """Draw all 6 faces of the 3D cube"""
        # Face definitions: (face_index, normal_vector, corner_positions)
        faces_3d = [
            # Up face (z=3)
            (0, [0, 0, 1], [(0, 0, 3), (3, 0, 3), (3, 3, 3), (0, 3, 3)]),
            # Down face (z=0)  
            (3, [0, 0, -1], [(0, 0, 0), (0, 3, 0), (3, 3, 0), (3, 0, 0)]),
            # Front face (y=0)
            (2, [0, -1, 0], [(0, 0, 0), (3, 0, 0), (3, 0, 3), (0, 0, 3)]),
            # Back face (y=3)
            (5, [0, 1, 0], [(3, 3, 0), (0, 3, 0), (0, 3, 3), (3, 3, 3)]),
            # Left face (x=0)
            (4, [-1, 0, 0], [(0, 3, 0), (0, 0, 0), (0, 0, 3), (0, 3, 3)]),
            # Right face (x=3)
            (1, [1, 0, 0], [(3, 0, 0), (3, 3, 0), (3, 3, 3), (3, 0, 3)])
        ]
        
        for face_idx, normal, corners in faces_3d:
            self._draw_3d_face(cube_state[face_idx], face_idx, corners)
    
    def _draw_3d_face(self, face, face_idx, corners):
        """Draw a single face in 3D"""
        # For simplicity, we'll just color the entire face with the center sticker color
        # In a more advanced implementation, you could draw individual stickers
        
        center_sticker = face[4]  # Center sticker (index 4)
        color = COLORS[center_sticker]
        
        # Create face vertices
        verts = [corners]
        
        # Add face to 3D plot
        from mpl_toolkits.mplot3d.art3d import Poly3DCollection
        face_collection = Poly3DCollection(verts, alpha=0.8, linewidths=2, edgecolors='black')
        face_collection.set_facecolor(color)
        self.ax.add_collection3d(face_collection)
    
    def animate_solve(self, initial_state, moves, title="Solving Animation"):
        """
        Animate the solving process (placeholder for future implementation)
        
        Args:
            initial_state: Starting cube state
            moves: List of moves to apply
            title: Title for the animation
        """
        print(f"Animation placeholder: {title}")
        print(f"Initial state: {initial_state}")
        print(f"Moves to animate: {moves}")
        # TODO: Implement step-by-step animation
    
    def compare_states(self, state1, state2, titles=["State 1", "State 2"]):
        """
        Compare two cube states side by side
        
        Args:
            state1: First cube state
            state2: Second cube state
            titles: Titles for each state
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 9))
        
        # Plot first state
        self._plot_single_net(state1, ax1, titles[0])
        
        # Plot second state
        self._plot_single_net(state2, ax2, titles[1])
        
        plt.tight_layout()
        plt.show()
        return fig
    
    def _plot_single_net(self, cube_state, ax, title):
        """Plot a single cube net on given axes"""
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 9)
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Face positions in the net
        face_positions = {
            0: (3, 6),  # Up
            1: (6, 3),  # Right
            2: (3, 3),  # Front
            3: (3, 0),  # Down
            4: (0, 3),  # Left
            5: (9, 3)   # Back
        }
        
        # Draw each face
        for face_idx, (start_x, start_y) in face_positions.items():
            self._draw_face_on_ax(cube_state[face_idx], start_x, start_y, ax)
        
        # Add title
        ax.text(6, 8.5, title, ha='center', va='center', fontsize=14, fontweight='bold')
    
    def _draw_face_on_ax(self, face, start_x, start_y, ax):
        """Draw a face on specific axes"""
        for i in range(3):
            for j in range(3):
                sticker_idx = i * 3 + j
                color = COLORS[face[sticker_idx]]
                
                x = start_x + j
                y = start_y + (2 - i)
                
                rect = patches.Rectangle((x, y), 1, 1, 
                                       linewidth=1, 
                                       edgecolor='black', 
                                       facecolor=color)
                ax.add_patch(rect)

def demo_visualization():
    """Demo function to show the visualization capabilities"""
    # Import solver components
    try:
        from solver.simple_solver import create_solved_cube, SimpleCubeSolver
    except ImportError:
        print("Could not import solver components for demo")
        return
    
    print("🎨 Cube Visualization Demo")
    print("=" * 30)
    
    # Create visualizer
    viz = CubeVisualizer()
    
    # Create a solved cube
    solved_cube = create_solved_cube()
    print("📊 Displaying solved cube...")
    viz.plot_2d_net(solved_cube, "Solved Rubik's Cube")
    
    # Create a scrambled cube
    solver = SimpleCubeSolver()
    scramble_moves = ["R", "U", "R'", "U'", "R", "R", "U", "R'", "U'"]
    scrambled_cube = solver.apply_moves(solved_cube, scramble_moves)
    print(f"📊 Displaying scrambled cube (moves: {' '.join(scramble_moves)})...")
    viz.plot_2d_net(scrambled_cube, f"Scrambled Cube - {' '.join(scramble_moves)}")
    
    # Compare states
    print("📊 Comparing solved vs scrambled...")
    viz.compare_states(solved_cube, scrambled_cube, 
                      ["Solved State", f"Scrambled - {' '.join(scramble_moves)}"])
    
    # Try 3D visualization
    try:
        print("📊 Displaying 3D cube...")
        viz.plot_3d_cube(solved_cube, "3D Solved Cube")
    except Exception as e:
        print(f"3D visualization not available: {e}")

if __name__ == "__main__":
    demo_visualization()