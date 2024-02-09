#!/usr/bin/python3
"""0-nqueens"""
import sys


def print_solutions(solutions):
    """print solution of nqueen"""
    for solution in solutions:
        print([list(position) for position in enumerate(solution)])


def is_valid_state(state, board_size):
    """Check if vertical and horizontal are valid positions"""
    return len(state) == board_size


def get_candidates(state, board_size):
    """get the list of valid positions"""
    if not state:
        return range(board_size)
    position = len(state)
    candidates = set(range(board_size))
    # prune down candidates
    for row, col in enumerate(state):
        candidates.discard(col)
        dist = position - row

        candidates.discard(col - dist)
        candidates.discard(col + dist)
    return candidates


def search(state, solutions, board_size):
    """Recursive search function"""
    if is_valid_state(state, board_size):
        solutions.append(state.copy())
        return

    for candidate in get_candidates(state, board_size):
        state.append(candidate)
        search(state, solutions, board_size)
        state.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    board_size = sys.argv[1]
    try:
        board_size = int(board_size)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    state = []

    search(state, solutions, board_size)

    print_solutions(solutions)
