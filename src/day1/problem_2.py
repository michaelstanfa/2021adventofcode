import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utility import *

def main():
    solve_problem()

def solve_problem():
    dir = os.path.abspath(os.curdir)
    file_name = "import.txt"
    
    list = load_file_return_as_list(dir, file_name)

    adjusted = []
    i = 2
    while i <= len(list) - 1:
        print(i)
        adjusted.append(int(list[i]) + int(list[i - 1]) + int(list[i - 2]))
        i += 1
    
    count_increased(adjusted)

def count_increased(array):
    increased = 0

    last_num = 0
    for depth in array:
        num = int(depth)
        if(int(num) > last_num):
            increased += 1

        last_num = num

    print(increased - 1)

if __name__ == '__main__':
    main()