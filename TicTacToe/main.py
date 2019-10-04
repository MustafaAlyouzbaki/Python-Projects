# This is my code for console tic tac toe that I basically transferred from Java
# to Python syntax, so I could practice and get better at Python
# Name: Mustafa Al-Youzbaki
# Date: Sept 29, 2019
import random

# Splash Screen
print("TIC TAC TOE")
print("Welcome to Tic Tac Toe, the board you will "
      "be playing on is a board that is numbered "
      "1-9, like a number pad. Simply select a "
      "number when it is your turn and play!")

# Global Variables
running = True
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

def print_board():
    global board
    print("\n| "+board[0]+" | "+board[1]+" | "+board[2]+" |")
    print("| "+board[3]+" | "+board[4]+" | "+board[5]+" |")
    print("| "+board[6]+" | "+board[7]+" | "+board[8]+" |\n")

def spot_available(spot):
    if(board[spot] == "-"):
        return True
    else:
        return False

def player_turn():
    # Input
    choice = int(input("Choose where to play (1-9): ")) - 1
    while not(spot_available(choice)):
        choice = int(input("\nChoose another spot (1-9): ")) - 1
    # Changing board
    board[choice] = "X"

def comp_turn():
    # "Input"
    choice = random.randrange(8)
    while not(spot_available(choice)):
        choice = random.randrange(8)
    # Changing board
    board[choice] = "O"

def is_three_in_row(line):
    if(line == "XXX" or line == "OOO"):
        return True

def game_won():
    # Rows
    line = board[0] + board[1] + board[2]
    if(is_three_in_row(line)): return True
    line = board[3] + board[4] + board[5]
    if (is_three_in_row(line)): return True
    line = board[6] + board[7] + board[8]
    if (is_three_in_row(line)): return True
    # Columns
    line = board[0] + board[3] + board[6]
    if (is_three_in_row(line)): return True
    line = board[1] + board[4] + board[7]
    if (is_three_in_row(line)): return True
    line = board[2] + board[5] + board[8]
    if (is_three_in_row(line)): return True
    # Diagonals
    line = board[0] + board[4] + board[8]
    if (is_three_in_row(line)): return True
    line = board[2] + board[4] + board[6]
    if (is_three_in_row(line)): return True

# Main game loop
while running:
    print_board()
    player_turn()
    if(game_won()):
        print("\nCongrats, you won!")
        running = False
        print_board()
    else:
        comp_turn()
        if(game_won()):
            print("\nBetter luck next time!")
            running = False
            print_board()