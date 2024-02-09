#!/usr/bin/python3
"""nqueen module"""
import sys
from typing import List, Mapping

def search(board: List[List], solutions: List[List], board_size: int, row: int, board_info: Mapping):
    """search for correct board"""
    if row == board_size:
        solutions.append(board.copy())
        return

    for col in range(board_size):
        if col in board_info["cols_set"] or row + col in board_info['neg_set'] or row - col in board_info['pos_set']:
            continue

        board_info['cols_set'].add(col)
        board_info['neg_set'].add(row + col)
        board_info['pos_set'].add(row - col)
        board.append([row, col])

        search(board, solutions, board_size, row + 1, board_info)
        
        board_info['cols_set'].remove(col)
        board_info['neg_set'].remove(row + col)
        board_info['pos_set'].remove(row - col)
        board.pop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueen N")
        sys.exit(1)

    board_size = sys.argv[1]
    try:
        board_size = int(board_size)
    except ValueError:
        print("N should be a number")
        sys.exit(1)

    solutions = []
    board = []
    board_info = {
        "cols_set": set(),
        "neg_set": set(),
        "pos_set": set(),
    }

    search(board, solutions, board_size, 0, board_info)

    for solution in solutions:
        print(solution)
