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

    count_of_inputs = len(inputs)
    result = [0] * len(inputs[0])
    matrix = []

    for input in inputs:
        matrix.append([int(a) for a in str(input)])

    for item in matrix:
        i = 0
        for digit in item:
            result[i] += digit
            i += 1

    gamma = [0] * len(inputs[0])
    epsilon = [0] * len(inputs[0])

    j = 0
    for number in result:
        
        if(number > count_of_inputs / 2):
            gamma[j] = '1'
            epsilon[j] = '0'
        else:
            gamma[j] = '0'
            epsilon[j] = '1'

        j+=1

    gamma_binary = '0b' + ''.join(gamma)
    epsilon_binary = '0b' + ''.join(epsilon)

    gamma_int = int(gamma_binary, 2)
    epsilon_int = int(epsilon_binary, 2)

    print(gamma_int * epsilon_int)


if __name__ == '__main__':
    main()