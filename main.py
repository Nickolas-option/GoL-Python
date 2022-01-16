#!/usr/bin/env python3
from board import Board
from console import clear_console, resize_console


def main():
    clear_console()
    user_rows = int(input('Please, enter the number of rows. Recommended size >=32\n'))
    user_columns = int(input('Please, enter the number of columns. Recommended size >=32\n'))
    clear_console()
    resize_console(user_rows, user_columns)

    game_of_life_board = Board(user_rows, user_columns)

    game_of_life_board.draw_board()

    user_action = ''
    while user_action != 'q':
        user_action = input('Press "Enter" for next step of the game or press "q" to stop.')

        if user_action == '':
            game_of_life_board.update_board()
            game_of_life_board.draw_board()


if __name__ == "__main__":
    main()
