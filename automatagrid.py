import numpy as np
from typing import TypeAlias
import constant

Moore: TypeAlias = tuple[bool, bool, bool, bool, bool]


def bool_to_str(b: bool) -> str:
    return '1' if b else '0'


def str_to_bool(s: str) -> bool:
    return True if s == '1' else False


def bools_to_int(bools: Moore) -> int:
    string_repres = bool_to_str(bools[0]) + \
                    bool_to_str(bools[1]) + \
                    bool_to_str(bools[2]) + \
                    bool_to_str(bools[3]) + \
                    bool_to_str(bools[4])
    return int(string_repres, 2)


class Cell:
    def __init__(self, state: bool = False):
        self.state = state

    def new_state(self, state: bool):
        self.state = state


class AutomataGrid:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.grid = np.empty((rows, cols), dtype=Cell)

    def fill_randomly(self):
        for r in range(self.rows):
            for c in range(self.cols):
                random_state = np.random.choice([True, False])
                self.grid[r, c] = Cell(random_state)

    @staticmethod
    def __rule(cells_states: Moore) -> bool:
        initial_rule_value = constant.RULE_VALUE
        num_of_state = bools_to_int(cells_states)
        bin_rule_value = format(initial_rule_value, f'0{constant.NUM_OF_DIGITS}b')
        string_result = bin_rule_value[num_of_state]
        return str_to_bool(string_result)

    def __cell_next_state(self, row: int, col: int):
        s_0, s_1, s_2, s_3, s_4 = self.grid[row, col], Cell(), Cell(), Cell(), Cell()
        # boundary conditions
        # not on the edge
        if 0 < row < self.rows - 1 and 0 < col < self.cols - 1:
            s_1 = self.grid[row + 1, col]
            s_2 = self.grid[row - 1, col]
            s_3 = self.grid[row, col - 1]
            s_4 = self.grid[row, col + 1]
        # on the edge
        else:
            # left bottom
            if row == 0 and col == 0:
                s_1 = self.grid[row + 1, col]
                s_2 = self.grid[self.rows - 1, 0]
                s_3 = self.grid[0, self.cols - 1]
                s_4 = self.grid[row, col + 1]
            # left top
            elif row == self.rows - 1 and col == 0:
                s_1 = self.grid[0, 0]
                s_2 = self.grid[row - 1, col]
                s_3 = self.grid[0, self.cols - 1]
                s_4 = self.grid[row, col + 1]
            # right top
            elif row == self.rows - 1 and col == self.cols - 1:
                s_1 = self.grid[0, self.cols - 1]
                s_2 = self.grid[row - 1, col]
                s_3 = self.grid[row, col - 1]
                s_4 = self.grid[self.rows - 1, 0]
            # right bottom
            elif row == 0 and col == self.cols - 1:
                s_1 = self.grid[row + 1, col]
                s_2 = self.grid[self.rows - 1, self.cols - 1]
                s_3 = self.grid[row, col - 1]
                s_4 = self.grid[0, 0]
            # not on the corner
            else:
                # bottom
                if row == 0:
                    s_1 = self.grid[row + 1, col]
                    s_2 = self.grid[self.rows - 1, col]
                    s_3 = self.grid[row, col - 1]
                    s_4 = self.grid[row, col + 1]
                # top
                elif row == self.rows - 1:
                    s_1 = self.grid[0, col]
                    s_2 = self.grid[row - 1, col]
                    s_3 = self.grid[row, col - 1]
                    s_4 = self.grid[row, col + 1]
                # left
                elif col == 0:
                    s_1 = self.grid[row + 1, col]
                    s_2 = self.grid[self.rows - 1, col]
                    s_3 = self.grid[row, self.cols - 1]
                    s_4 = self.grid[row, col + 1]
                # right
                elif col == self.cols - 1:
                    s_1 = self.grid[0, col]
                    s_2 = self.grid[row - 1, col]
                    s_3 = self.grid[row, col - 1]
                    s_4 = self.grid[row, 0]

        moore_neighbourhood = (s_0.state, s_1.state, s_2.state, s_3.state, s_4.state)
        self.grid[row, col].new_state(self.__rule(moore_neighbourhood))

    def next_iteration(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.__cell_next_state(row, col)

