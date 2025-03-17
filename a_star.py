import heapq
import numpy as np


class Node():
    def __init__(self, parent=None, pos=None):
        self.parent=parent
        self.pos = pos
        self.g = 0
        self.h = 0
        self.f = 0

def heuristic(a,b):
    distance = np.linalg.norm(a-b)
    return distance

def a_star(start, goal, grid):
    # Make start and end node
    start_node = Node(None, start)
    goal_node = Node(None, goal)
    path = []

    # queue
    queue = [start_node]
    visited = []

    #list to check neighbors:
    nbhrs = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

    while queue:
        # use f to pick "best" partial path N from queue
        N = 0
        
        # If node = goal, return oath
        if(curr_node.pos==goal_node.pos):
            child = curr_node
            while child:
                path.append(child.pos)
                child = child.parent
            return path[::-1] 
        
        # Else remove N from queue
        curr_node = queue.pop(N)

        # If N is in visited, go back to beginning
        if N in visited:
            pass
        
        # Else find children and add to queue
        else: 
            pos = curr_node.pos
            for nbhr in nbhrs:
                child_pos = (pos[0]+nbhr[0], pos[1]+nbhr[1])
                



    return path

