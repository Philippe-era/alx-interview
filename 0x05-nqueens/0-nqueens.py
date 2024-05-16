#!/usr/bin/python3
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board_chess = []
    [board_chess.append([]) for initial in range(n)]
    [row.append(' ') for initial in range(n) for row in board_chess]
    return (board_chess)


def board_deepcopy(board):
    """displays the chess board"""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """solutions to the chess board"""
    solution_chess = []
    for ring in range(len(board)):
        for col in range(len(board)):
            if board[ring][col] == "Q":
                solution_chess.append([ring, col])
                break
    return (solution_chess)


def xout(board, row, col):
    """The chessboard is finished
    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    for colom in range(col + 1, len(board)):
        board[row][colom] = "x"
    for colom in range(col - 1, -1, -1):
        board[row][colom] = "x"
    for ring in range(row + 1, len(board)):
        board[ring][col] = "x"
    # X out all spots above
    for ring in range(row - 1, -1, -1):
        board[ring][col] = "x"

    colom = col + 1
    for ring in range(row + 1, len(board)):
        if colom >= len(board):
            break
        board[ring][colom] = "x"
        colom += 1

    colom = col - 1
    for ring in range(row - 1, -1, -1):
        if colom < 0:
            break
        board[ring][colom]
        colom -= 1
    # X out all spots diagonally up to the right
    colom = col + 1
    for ring in range(row - 1, -1, -1):
        if colom >= len(board):
            break
        board[ring][colom] = "x"
        colom += 1
    
    colom = col - 1
    for ring in range(row + 1, len(board)):
        if colom < 0:
            break
        board[ring][colom] = "x"
        colom -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for colom in range(len(board)):
        if board[row][colom] == " ":
            part_board = board_deepcopy(board)
            part_board[row][colom] = "Q"
            xout(part_board, row, colom)
            solutions = recursive_solve(part_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions_curve = recursive_solve(board, 0, 0, [])
    for solo in solutions_curve:
        print(solo)
