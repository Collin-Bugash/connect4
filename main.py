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
            lines.append([*line[:-1]])
            if len(line[:-1]) == 0:
                next_move = line[0]
            else:
                for spot in line:
                    if spot != "0":
                        move_number += 1

        board = [[int(i) for i in line] for line in lines[:-1]]
        board = np.array(board)

    return board, int(next_move), move_number

def interactive():
    board, next_move, move_number = init()

    scores = [get_score(board, 1), get_score(board, 2)]

    # while True:
    if next_move == 1:
        # Handle computer turn
        if print_info(board, scores) == -1:
            sys.exit()

    else:
        # Handle human turn
        print("Human turn")

def print_info(board, scores):
    print("Board State:")
    for line in board:
        # Print line excluding \n
        print(line)
    print(f"Player 1 Score: {scores[0]}")
    print(f"Player 2 Score: {scores[1]}")
    if np.any(board == 0) != True:
        print("Board is full, ending game.")
        return -1

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

def computer_move(board):
    return 1
    
interactive()





