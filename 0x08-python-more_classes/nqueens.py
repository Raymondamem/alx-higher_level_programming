#!/usr/bin/python3

import sys

def solve_nqueens(n):
    def can_place(pos, ocuppied_positions):
        for i in range(len(ocuppied_positions)):
            if ocuppied_positions[i] == pos or \
                ocuppied_positions[i] - i == pos - len(ocuppied_positions) or \
                ocuppied_positions[i] + i == pos + len(ocuppied_positions):
                return False
        return True

    def place_queen(n, index, ocuppied_positions, all_ocuppied_positions):
        if index == n:
            all_ocuppied_positions.append(ocuppied_positions[:])
            return
        for i in range(n):
            if can_place(i, ocuppied_positions):
                ocuppied_positions.append(i)
                place_queen(n, index + 1, ocuppied_positions, all_ocuppied_positions)
                ocuppied_positions.pop()

    all_ocuppied_positions = []
    place_queen(n, 0, [], all_ocuppied_positions)
    return all_ocuppied_positions

def print_result(all_ocuppied_positions):
    result = []
    for ocuppied_positions in all_ocuppied_positions:
        temp = []
        for i in range(len(ocuppied_positions)):
            temp.append([i, ocuppied_positions[i]])
        result.append(temp)
    print(result)

n = 4
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)

all_ocuppied_positions = solve_nqueens(n)
print_result(all_ocuppied_positions)

