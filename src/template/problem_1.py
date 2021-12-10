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

if __name__ == '__main__':
    main()