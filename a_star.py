import heapq
import numpy as np


def heuristic(a,b):
    distance = np.linalg.norm(a-b)
    return distance

def a_star(start, goal, grid):
    queue = [start]
    visited = []
    while queue:
        coord = queue.pop(0)

