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
    def __init__(self):
        self.state = False

    def __init__(self, state: bool):
        self.state = state

    def new_state(self, state: bool):
        self.state = state


class Grid:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.grid = np.empty((rows, cols), dtype=Cell)

    @staticmethod
    def __rule(cells_states: Moore) -> bool:
        initial_rule_value = constant.RULE_VALUE
        num_of_state = bools_to_int(cells_states)
        bin_rule_value = format(initial_rule_value, f'0{constant.NUM_OF_DIGITS}b')
        string_result = bin_rule_value[num_of_state]
        return str_to_bool(string_result)

    def __cell_next_state(self, row: int, col: int):
        if 0 < row < self.rows - 1 and 0 < col < self.cols - 1:
            s_0 = self.grid[row, col]
            s_1 = self.grid[row + 1, col]
            s_2 = self.grid[row - 1, col]
            s_3 = self.grid[row, col - 1]
            s_4 = self.grid[row, col + 1]
            moore_neighbourhood = (s_0.state, s_1.state, s_2.state, s_3.state, s_4.state)
            self.grid[row, col].new_state(self.__rule(moore_neighbourhood))
        else:
            pass
