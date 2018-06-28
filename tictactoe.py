#from IPython.display import clear_output
import os
import random


def display_board(board):
    print("\n"*100)
    print("\t  |   |")
    print("\t"+board[1] + " | " + board[2] + " | " + board[3])
    print("\t  |   |")
    print("\t- - - - -")
    print("\t  |   |")
    print("\t"+board[4] + " | " + board[5] + " | " + board[6])
    print("\t  |   |")
    print("\t- - - - -")
    print("\t  |   |")
    print("\t"+board[7] + " | " + board[8] + " | " + board[9])
    print("\t  |   |")
    print("\n")

def player_input(player1name):
    '''
    OUTPUT: (player1,player2)
    '''
    player1 = ''

    while player1 != 'X' and player1 != 'O':
        player1 = input("\n"+player1_name+" choose X or O: ").upper()
    if player1 == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    r1 = board[1] == board[2] == board[3] == mark
    r2 = board[4] == board[5] == board[6] == mark
    r3 = board[7] == board[8] == board[9] == mark
    c1 = board[1] == board[4] == board[7] == mark
    c2 = board[2] == board[5] == board[8] == mark
    c3 = board[3] == board[6] == board[9] == mark
    diag1 = board[1] == board[5] == board[9] == mark
    diag2 = board[3] == board[5] == board[7] == mark

    if r1 or r2 or r3 or c1 or c2 or c3 or diag1 or diag2:
        return True


def choose_first():
    choose = random.randint(1,2)
    if choose == 1 :
        return "Player1"
    else:
        return "Player2"


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    #position = 0
    for i in [1,2,3,4,5,6,7,8,9]:
        if space_check(board,i):
            return False
    # Return True if board is full
    return True


def player_choice(board,player,move):
    position = 0
    while((position not in range(1,10)) or (not space_check(board,position))):
        position = int(input("{} make your move no. {}:".format(player,move)))
    return position


def replay():
    ask = input("\n\nWant to play again(Y/N): ")
    return ask == 'Y' or ask == 'y'


##TIC TAC TOE

print("\n\t\tWELCOME TO THE GAME TIC TAC TOE!\n")

while True:
    # SETUP THE GAME

    my_board = [" "] * 10

    player1_name = input("Player 1, Enter your name: ")
    player2_name = input("Player 2, Enter your name: ")

    player1, player2 = player_input(player1_name)

    chance = choose_first()
    if chance == "Player1":
        print("\n"+player1_name+" goes first!")
    else:
        print("\n"+player2_name+" goes first!")


    ask = input("\nReady to play the game? (y/n): ")

    if ask == 'y':
        game_on = True
    else:
        game_on = False

    move_2_no = 0
    move_1_no = 0

    while game_on:
        # Player 1 chance
        if chance == "Player1":
            # Display the board
            display_board(my_board)

            # Ask for position

            move_1_no += 1
            pos = player_choice(my_board, player1_name,move_1_no)

            # Place the marker

            place_marker(my_board, player1, pos)

            # Check if player1 wins

            if win_check(my_board, player1):
                display_board(my_board)
                print("\n\t"+player1_name.upper()+" HAS WON!!")
                game_on = False
            else:
                if full_board_check(my_board):
                    display_board(my_board)
                    print("\n\tTIE GAME!")
                    game_on = False

                else:
                    chance = "Player2"


        else:
            # Display the board
            display_board(my_board)

            # Ask for position
            move_2_no += 1
            pos = player_choice(my_board, player2_name,move_2_no)

            # Place the marker

            place_marker(my_board, player2, pos)

            # Check if player2 wins

            if win_check(my_board, player2):
                display_board(my_board)
                print("\n\t"+player2_name.upper()+" HAS WON!!")
                game_on = False
            else:
                if full_board_check(my_board):
                    display_board(my_board)
                    print("\n\tTIE GAME!")
                    game_on = False

                else:
                    chance = "Player1"

    if not replay():
        break;
