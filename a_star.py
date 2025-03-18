import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps
from queue import PriorityQueue

class Node():
    def __init__(self, parent=None, pos=None):
        self.parent=parent
        self.pos = pos
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.pos==other.pos

    def __lt__(self,other):
        return self.f < other.f

def heuristic(a,b):
    a_np = np.array(a)
    b_np = np.array(b)
    distance = np.linalg.norm(a_np-b_np)
    return distance

def a_star(start, goal, grid):
    # Make start and end node
    start_node = Node(None, start)
    goal_node = Node(None, goal)
    path = []

    x_max = grid.shape[0]-1
    y_max = grid.shape[1]-1

    # queue
    queue = PriorityQueue()
    queue.put(start_node)
    visited = []

    #list to check neighbors:
    nbhrs = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

    while not queue.empty():
        curr_node = queue.get()

        # If node = goal, return oath
        if(curr_node.pos==goal_node.pos):
            child = curr_node
            while child:
                path.append(child.pos)
                child = child.parent
            return path[::-1]

        # If N is in visited, go back to beginning
        if curr_node in visited:
            pass
        # Else find all children NOT in expanded and is a a valid grid location
        else:
            visited.append(curr_node)
            pos = curr_node.pos
            for nbhr in nbhrs:
                child_pos = (pos[0]+nbhr[0], pos[1]+nbhr[1])
                child_node = Node(curr_node, child_pos)
                if child_node in visited:
                    pass
                elif child_pos[0] < 0 or child_pos[0] > x_max or child_pos[1]<0 or child_pos[1]>y_max:
                    pass
                elif grid[child_pos[0]][child_pos[1]] == 1 :
                    pass
                else:
                    child_node.g = curr_node.g+1
                    child_node.h = heuristic(child_pos, goal)
                    child_node.f = child_node.g+child_node.h
                    queue.put(child_node)
    print('failure')
    return path
