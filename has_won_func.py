
board = [['o','x','o'],
         ['o','x','x'],
         ['x','o','o']]
letter = 'x'


def won(board, letter):
    boards =[
        board,
        [[board[j][i] for i in range(3)] for j in range(3)], # Flipped board.
        [[board[j][j] for j in range(3)] for i in range(0, 2, 1)] # Diagnols.
    ]

    for board in boards:
        for i in range(3):
            if set(board[i]) == set(letter):
                return True
