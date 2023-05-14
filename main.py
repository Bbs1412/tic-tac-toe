import copy
import time
import random

board=[[" " for j in range(3)] for i in range (3)]
# print(board)
empty_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
demo_board = [[' ', 'X', ' '], ['O', 'X', 'X'], [' ', 'X', 'O']]

instruct="""\nThe board is like this:
     1     2    3
   ----------------
 1 | 11 | 12 | 13 |
   ----------------
 2 | 21 | 22 | 23 |
   ----------------
 3 | 31 | 32 | 33 |
   ----------------
"""

""" BoardStyle 1:
# board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    0   1   2
 0  X |   |   
   -----------
 1  O | X |   
   -----------
 2    |   | X 

def print_board(board):
    print("   0   1   2")
    for i in range(3):
        print(i,end="  ")
        print(*board[i],sep=" | ")
        if i!=2:
            print("  -----------")
print_board(board)
"""

""" BoardStyle 2:
     0   1   2
   -------------
 0 | X |   |   |
   -------------
 1 | O | X |   |
   -------------
 2 |   |   | X |
   -------------
"""
def print_board(board):
    print("    1   2   3")
    print("  -------------")
    for i in range(3):
        print(i+1,*board[i],"",sep=" | ")
        print("  -------------")
# print_board(board)

def start_game():
    print("\nWelcome to the game!")
    time.sleep(1)
    print(instruct)
    time.sleep(3)

    z=random.randint(1,2)
    if z==1:
        print("Player \"X\" starts the game.")
        print_board(board)
        return "X"
    else:
        print("Player \"O\" starts the game")
        print_board(board)
        return "O"
curr_player=start_game()


def switch_player(curr_player):
    if curr_player=="X":
        print("\nO's turn:")
        return "O"
    else:
        print("\nX's turn:")
        return "X"
# curr_player=switch_player(curr_player)

val_ip=[11,12,13,21,22,23,31,32,33]
curr_val_ip=copy.deepcopy(val_ip)


def take_input(curr_player):
    # Take valid input:
    while (True):
        print("Input possibilities are:",curr_val_ip)
        print("Enter position: ",end="")
        n=int(input())
        if n not in curr_val_ip:
            # print(f"Invalid input, must be from: {curr_val_ip}\nTry again: ")
            print("\nInvalid input; Try again:")
        else:
            curr_val_ip.remove(n)
            break

    # Update data 
    i=(n//10)-1     #(31 -> 3-1 -> 2)
    j=(n%10)-1      #(31 -> 1-1 -> 0)
    board[i][j]=curr_player
# take_input(curr_player)

def check_win(board):
    def three(a,b,c):
        i1,i2,i3=(a//10)-1,(b//10)-1,(c//10)-1
        j1,j2,j3=(a%10)-1,(b%10)-1,(c%10)-1
        
        if board[i1][j1]==board[i2][j2] and board[i1][j1]==board[i3][j3] and board[i2][j2]!=" ":
            return True
        else:
            return False

    if three(11,12,13) or three(21,22,23) or three(31,32,33) or three(11,21,31) or three(12,22,32) or three(13,23,33) or three(11,22,33) or three(13,22,31):
        return True
    else:
        return False
    
while (True):
    # curr_player=start_game()      # Called in code already
    take_input(curr_player)
    print_board(board)
    if(check_win(board)):
        print(f"Player {curr_player} won the game!!")
        break
    if (curr_val_ip==[]):
        print("Game TIE!!")
        break
    curr_player=switch_player(curr_player)

