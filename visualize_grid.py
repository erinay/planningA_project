import numpy as np
import matplotlib.pyplot as plt
from a_star import a_star

def plot_grid(grid, start, goal, path=None):
    plt.imshow(grid, cmap='YlGn')

    # Plot start and goal
    plt.scatter(start[1], start[0], marker="o", color="green", label="Start")
    plt.scatter(goal[1], goal[0], marker="x", color="red", label="Goal")

    # Plot path
    if path:
        for (x, y) in path:
            plt.scatter(y, x, marker=".", color="blue")

    plt.legend()
    plt.grid(True, which='both', color='gray', linestyle='-', linewidth=0.5)
    plt.show()


N = 20
gridsize = (N,N+10)
grid = np.zeros(gridsize)

## Add obstacles
grid[3, 3:7] = 1

start = (N-1,N+10-1)
goal = (3, 8)

path = a_star(start, goal, grid)
plot_grid(grid, start, goal, path)
