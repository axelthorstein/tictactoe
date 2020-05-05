 

# Obectives:
# 
# - Something to handle the board - check
# - Something to take user input - check
#   - Do error checking on user input - check
# - Something to switch turns between players
# - Something to decide if the game is over
# - Something to catch if a move has already been called

def get_move():
    letter = input('Please input X or O: ')
    while letter not in ('X', 'O'):
      letter = input('Please input X or O (be aware of capitalization): ')
    return letter
  

def get_place():
    row = input('Please input what row you would like to place: ')
    while row not in ('0', '1', '2'):
      row = input('Please select 0, 1, or 2 for your row: ')
    column = input('Please input what column you would like to place: ')
    while column not in ('0', '1', '2'):
      column = input('Please select 0, 1, or 2 for your column: ')
    return [int(row), int(column)]


def make_board():
    return [['-', '-', '-'],
            ['-', '-', '-'], 
            ['-', '-', '-']]


def view_board(board):
    print(board[0])
    print(board[1])
    print(board[2])
    return


def check_x_winner(board):
    for space in board:
        if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
            return "X Player, You Are The Ultimate Tic-Tac-Toe CHAMPION"
        elif board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
            return "X Player, You Are The Ultimate Tic-Tac-Toe CHAMPION"
        elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
            return "X Player, You Are The Ultimate Tic-Tac-Toe CHAMPION"
        elif board[1][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
            return "X Player, You Are The Ultimate Tic-Tac-Toe CHAMPION"
        elif board[0][2] == 'X'and board[1][1] == 'X' and board[2][2] == 'X':
            return "X Player, You Are The Ultimate Tic-Tac-Toe CHAMPION"
        else:
            return "No 1 Has 1"
        

def check_o_winner(board):
    for space in board:
        if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
            return "O Player, You Are The Ultimate Tic-Tac-Toe CHAMPION"
        elif board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
            return "O Player, You Are The Ultimate Tic-Tac-Toe CHAMPION"
        elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
            return "O Player, You Are The Ultimate Tic-Tac-Toe CHAMPION"
        elif board[1][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
            return "O Player, You Are The Ultimate Tic-Tac-Toe CHAMPION"
        elif board[0][2] == 'O'and board[1][1] == 'O' and board[2][2] == 'O':
            return "O Player, You Are The Ultimate Tic-Tac-Toe CHAMPION"
        else:
            return "No 1 Has 1"


#this is how players interact with the game
def apply_move():
#takes the input of X or 0
    move = get_move()
#takes the row and column, where user would like to place move
    place = get_place()
#updates the board within view_board
    board[int(place[0])][int(place[1])] = move
#user check the board
    check_x_winner(board)
    check_o_winner(board)
    view_board(board)


def main():
    board = make_board()
    apply_move()



if __name__ == '__main__':
  main()
    
#first attempted check method
''''
def check_x_winner(board):
    for space in board:
        if board[0][0] == 'X':
          if board[1][1] == 'X':
            if board[2][2] == 'X':
              return "X Player, You Are The Ultimate Tic-Tac-Toe CHAMPION"
            else:
              return view_board(board)
          elif board[0][1] == 'X':
            if board[0][2] == 'X':
              return "X Player, You Are The Ultimate Tic-Tac-Toe CHAMPION"
            else:
              return view_board(board)
          else:
              return view_board(board)
        elif board[0][2] == 'X':
          if board[1][1] == 'X':
            if board[2][0] == 'X':appl
              return "X Player, You Are The Ultimate Tic-Tac-Toe CHAMPION"
            return view_board(board)
          return view_board(board)
        elif board[1][0] == 'X':
          if board[0][1] == 'X':
            if board[0][2] == 'X':
              return "X Player, You Are The Ultimate Tic-Tac-Toe CHAMPION"
            else:
              return view_board(board)
          else:
            return view_board(board)
        elif board[0][2] == 'X':
          if board[1][1] == 'X':
            if board[2][2] == 'X':
              return "X Player, You Are The Ultimate Tic-Tac-Toe CHAMPION"
            else:
              return view_board(board)
          else:
            return view_board(board)
        else:
          return view_board(board)
'''
  
