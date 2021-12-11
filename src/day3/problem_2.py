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

    matrix = []

    for input in inputs:
        matrix.append([int(a) for a in str(input)])

    print(matrix)
    
    oxygen = evaluate_matricies(matrix, 0, 'greater', 1)
    co2 = evaluate_matricies(matrix, 0, 'fewer', 0)

    oxygen_string = [str(a) for a in oxygen]
    co2_string = [str(a) for a in co2]

    oxygen_binary = '0b' + ''.join(oxygen_string)
    co2_binary = '0b' + ''.join(co2_string)

    oxygen_decimal = int(oxygen_binary, 2)
    co2_decimal = int(co2_binary, 2)

    print(f"oxygen: {oxygen_decimal}")
    print(f"co2: {co2_decimal}")

    print(f"total: {oxygen_decimal * co2_decimal}")

def evaluate_matricies(set_of_lists, index_to_check, greater_or_fewer, tie_breaker):

    if len(set_of_lists) == 1:
        return set_of_lists[0]

    zeroes = 0
    ones = 0
    keep = 2

    for list in set_of_lists:

        if list[index_to_check] == 0:
            zeroes += 1
        else:
            ones += 1

    if zeroes == ones:
        keep = tie_breaker
    elif greater_or_fewer == 'greater':
        keep = return_greater_count(zeroes, ones)
    else:
        keep = return_fewer_count(zeroes, ones)

    updated_set_of_lists = []

    for item in set_of_lists:
        if(item[index_to_check] == keep):
            updated_set_of_lists.append(item)

    return evaluate_matricies(updated_set_of_lists, index_to_check + 1, greater_or_fewer, tie_breaker)

def return_greater_count(zeroes, ones):
    
    if(zeroes > ones):
        return 0
    
    return 1

def return_fewer_count(zeroes, ones):
    
    if(zeroes < ones):
        return 0
    
    return 1

if __name__ == '__main__':
    main()