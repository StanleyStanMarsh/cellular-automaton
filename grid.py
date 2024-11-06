import numpy as np


class Cell:
    def __init__(self):
        self.state = False

    def __init__(self, state: bool):
        self.state = state


class Grid:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.grid = np.empty((rows, cols), dtype=Cell)
