#Project 3
 #Function to display the board
import random
from random import random
def display_board(board):
    print()
    print(board[0],"|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3],"|",board[4],"|",board[5])
    print("--+---+--")
    print(board[6],"|",board[7],"|",board[8])
    print()
#Function to check winner
def check_winner(board,mark):
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6) ]
    for pos in win_positions:
        if board[pos[0]]==board[pos[1]]==board[pos[2]]==mark:
          return True
    return False
# function to check draw
def is_draw(board):
    return""not in board
# function for player move
def player_move(board):
    while True:
        move=int(input("Enter your position(1-9):"))-1
        if 0<=move <=8 and board[move]==" ":
            board[move]="X"
            break
        else:
            print("Invalid move!Try again")
#Function for Computer move
def computer_move(board):
    empty_positions =[i for i in range(9)if board[i]==" "]
    move = random.choice(empty_positions)
    board[move]="0"
    print("Computer chose position:",move+1)
#Main game function
def play_games():
    board = [" "]*9
    print("Welcome to Tic-Tac-Toe")
    print("You are X,Computer is 0")
    display_board(board)
    while True:
        player_move(board)
        display_board(board)
        if check_winner(board,"X"):
            print("Congratulations! dear you win")
            break
        if is_draw(board):
           print("It is a draw")
           break
        computer_move(board)
        display_board(board)
        if check_winner(board,"0"):
            print("Computer wins!Best of luck for next")
            break
        if is_draw(board):
           print("Its a draw")
           break