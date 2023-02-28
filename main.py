import sys
import numpy as np
from scipy.signal import convolve2d

# python main.py interactive [input_file] [computer-next/human-next] [depth]
# argv[1] = main.py, argv[2] = interactive, argv[3] = input_file, argv[4] = next_move, argv[5] = depth

def init():
    move_number = 0
    lines = []
    with open('board.txt', 'r') as initial_board:
        # Create initial state
        for line in initial_board:
            lines.append(line)
            for spot in line:
                if spot == "1":
                    move_number += 1
        # Set initial board to all lines except last
        board = lines[:-1]
        # Get who initially moves
        next_move = int(lines[-1])

    return board, next_move, move_number

def interactive():
    board, next_move, move_number = init()

    while True:
        if next_move == 1:
            print("computer is next")
        else:
            print("human is next")

def print_board(board):
    for line in board:
        # Print line excluding \n
        print(line[:-1])

def get_score(board, player):
    score = 0
    horizontal_kernel = np.array([[ 1, 1, 1, 1]])
    vertical_kernel = np.transpose(horizontal_kernel)
    diag1_kernel = np.eye(4, dtype=np.uint8)
    diag2_kernel = np.fliplr(diag1_kernel)
    detection_kernels = [horizontal_kernel, vertical_kernel, diag1_kernel, diag2_kernel]

    for kernel in detection_kernels:
        score += np.sum(convolve2d(board == player, kernel, mode="valid") == 4)
    return score
    


lines = []
with open('board.txt', 'r') as initial_board:
    # Create initial state
    for line in initial_board:
        lines.append([*line[:-1]])
    lines = lines[:-1]
    # Get who initially moves
lines = [int(i) for i in lines]

print(lines)
# print(f"Score: {get_score(board, 1)}")