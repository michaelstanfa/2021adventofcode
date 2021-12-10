import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utility import *

def main():
    solve_problem()

def solve_problem():
    dir = os.path.abspath(os.curdir)
    file_name = "import.txt"
    inputs = load_file_return_as_list(dir, file_name)

    x_axis = 0
    y_axis = 0
    depth = 0

    for input in inputs:
        direction = input.split(" ")[0]
        quantity = int(input.split(" ")[1])
        
        if direction == "forward":
            x_axis += quantity
        elif direction == "down":
            y_axis += quantity
        else:
            y_axis -= quantity

    print(y_axis * x_axis)

if __name__ == '__main__':
    main()