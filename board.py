import random

import console
from cell import Cell


class Board:
    def __init__(self, rows, columns):

        self._rows = rows
        self._columns = columns
        self._grid = [[Cell() for column_cells in range(self._columns)] for row_cells in range(self._rows)]
        self._generate_board()

    def draw_board(self):
        console.clear_console()

        for row in self._grid:
            for column in row:
                print(column.print_me(), end='')
            print()

    def _generate_board(self):
        """
        генерация изначального положения клеток
        """

        for row in self._grid:
            for cell in row:
                # 33.3% шанс стать живой
                chance_number = random.randint(0, 2)
                if chance_number == 0:
                    cell.set_alive()

    def check_neighbour(self, check_row, check_column):

        neighbour_list = []

        for row in range(-1, 2):
            for column in range(-1, 2):
                neighbour_row = check_row + row
                neighbour_column = check_column + column

                valid_neighbour = True

                if neighbour_row == check_row and neighbour_column == check_column:
                    valid_neighbour = False

                if neighbour_row < 0 or neighbour_row >= self._rows:  # ????? ?? ???????
                    valid_neighbour = False

                if neighbour_column < 0 or neighbour_column >= self._columns:  # ????? ?? ???????
                    valid_neighbour = False

                if valid_neighbour:
                    neighbour_list.append(self._grid[neighbour_row][neighbour_column])

        return neighbour_list

    def update_board(self):

        to_be_alive = []
        to_be_killed = []

        for row in range(len(self._grid)):
            for column in range(len(self._grid[row])):
                check_neighbour = self.check_neighbour(row, column)

                living_neighbours_count = []

                for neighbour_cell in check_neighbour:
                    if neighbour_cell.is_alive():
                        living_neighbours_count.append(neighbour_cell)

                # ???? ??????????????? ??????
                cell_object = self._grid[row][column]
                main_cell_is_alive = cell_object.is_alive()

                if main_cell_is_alive:
                    if len(living_neighbours_count) < 2 or len(living_neighbours_count) > 3:
                        # убиваем
                        to_be_killed.append(cell_object)
                    else:
                        to_be_alive.append(cell_object)
                else:
                    # оживляем
                    if len(living_neighbours_count) == 3:
                        to_be_alive.append(cell_object)

        for cell_items in to_be_alive:
            cell_items.set_alive()

        for cell_items in to_be_killed:
            cell_items.set_dead()
