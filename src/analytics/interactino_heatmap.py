# interaction_heatmap.py

import numpy as np
import matplotlib.pyplot as plt

class InteractionHeatmap:
    def __init__(self, grid_size=(10, 10)):
        # Initialize a grid to represent the VR space
        self.grid = np.zeros(grid_size)

    def log_interaction(self, x, y):
        # Update heatmap at specified coordinates
        if 0 <= x < self.grid.shape[0] and 0 <= y < self.grid.shape[1]:
            self.grid[x, y] += 1
            print(f"Logged interaction at ({x}, {y}).")

    def display_heatmap(self):
        # Display heatmap using matplotlib
        plt.imshow(self.grid, cmap="hot", interpolation="nearest")
        plt.colorbar(label="Interaction Frequency")
        plt.title("Interaction Heatmap")
        plt.show()

# Usage example
heatmap = InteractionHeatmap(grid_size=(10, 10))
# Simulate interactions in the VR space
heatmap.log_interaction(3, 4)
heatmap.log_interaction(7, 8)
heatmap.log_interaction(3, 4)
heatmap.display_heatmap()

