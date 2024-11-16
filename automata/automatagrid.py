import numpy as np
from typing import TypeAlias
import automata.constant as const

Neumann: TypeAlias = tuple[bool, bool, bool, bool, bool]


def bool_to_str(b: bool) -> str:
    return '1' if b else '0'


def str_to_bool(s: str) -> bool:
    return True if s == '1' else False


def bools_to_int(bools: Neumann) -> int:
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
        for r in range(rows):
            for c in range(cols):
                self.grid[r, c] = Cell(False)

    def fill_randomly(self):
        for r in range(self.rows):
            for c in range(self.cols):
                random_state = np.random.choice([True, False])
                self.grid[r, c].new_state(random_state)

    @staticmethod
    def __rule(cells_states: Neumann) -> bool:
        initial_rule_value = const.RULE_VALUE
        num_of_state = bools_to_int(cells_states)
        bin_rule_value = format(initial_rule_value, f'0{const.NUM_OF_DIGITS}b')
        string_result = bin_rule_value[num_of_state]
        return str_to_bool(string_result)

    def __cell_next_state(self, row: int, col: int) -> Cell:
        num_rows = self.rows
        num_cols = self.cols

        # Get the current cell and its neighbors using modular arithmetic for wrapping
        s_0 = self.grid[row, col]
        s_1 = self.grid[(row + 1) % num_rows, col]  # Down
        s_2 = self.grid[(row - 1) % num_rows, col]  # Up
        s_3 = self.grid[row, (col - 1) % num_cols]  # Left
        s_4 = self.grid[row, (col + 1) % num_cols]  # Right

        # Collect the states of the Neumann neighborhood
        neumann_neighbourhood = (s_0.state, s_1.state, s_2.state, s_3.state, s_4.state)
        return Cell(self.__rule(neumann_neighbourhood))

    def next_iteration(self):
        grid_copy = np.empty((self.rows, self.cols), dtype=Cell)
        for row in range(self.rows):
            for col in range(self.cols):
                grid_copy[row, col] = self.__cell_next_state(row, col)
        self.grid = grid_copy

    # def is_empty(self) -> bool:
    #     return self.grid[0, 0] is None

    def set_state(self, row: int, col: int, state: bool):
        self.grid[row, col].new_state(state)

    def get_state(self, row: int, col: int) -> bool:
        return self.grid[row, col].state

    def __str__(self) -> str:
        result = []
        for row in range(self.rows):
            row_state = []
            for col in range(self.cols):
                cell = self.grid[row, col]
                row_state.append('1' if cell.state else '0')
            result.append(' '.join(row_state))
        return '\n'.join(result)

