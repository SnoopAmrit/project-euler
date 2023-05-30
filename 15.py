"""
Problem 15: Euler Project
    Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


    How many such routes are there through a 20×20 grid?
"""

import sys

def get_factorical(x: int) -> int:
    if x == 1:
        return 1
    
    return x * get_factorical(x-1)

def get_combinations(width: int, height: int) -> int:
    return int(get_factorical(width + height) / (get_factorical(width) * get_factorical(height)))

if __name__ == '__main__':
    width = int(sys.argv[1])
    height = int(sys.argv[2])

    print(get_combinations(width, height))

