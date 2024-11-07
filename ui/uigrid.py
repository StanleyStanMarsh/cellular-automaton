import copy
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout, QSlider
from automata.automatagrid import AutomataGrid


class UIGrid(QWidget):
    def __init__(self, m: int = 2, n: int = 2, iterations: int = 1):
        super().__init__()
        self.generate_button = QPushButton('Сгенерировать')
        self.reset_button = QPushButton('Очистить')
        self.calc_iterations_button = QPushButton('Просчитать итерации')
        self.iterations_slider = QSlider(Qt.Orientation.Horizontal)
        self.grid_layout = QGridLayout()
        self.is_clickable = False
        self.m = m
        self.n = n
        self.iterations = iterations
        self.grid = AutomataGrid(m, n)
        self.grids = [self.grid]
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        # grid of buttons
        self.grid_layout = QGridLayout()

        # fill with QPushButton
        for row in range(self.m):
            for col in range(self.n):
                button = QPushButton('')
                minimize_coefficient = max(self.m / 2, self.n / 2)
                button.setFixedSize(int(250 / minimize_coefficient), int(250 / minimize_coefficient))
                button.setStyleSheet('QPushButton {background-color: #FFFFFF}')
                button.setEnabled(self.is_clickable)
                # save button position
                button.setProperty('position', (row, col))
                # connect button click event with button_clicked()
                button.clicked.connect(lambda checked, b=button: self.button_clicked(b))
                self.grid_layout.addWidget(button, row, col)

        # add grid to main layout
        main_layout.addLayout(self.grid_layout)

        # -------------- control buttons --------------
        control_layout = QHBoxLayout()

        self.generate_button.clicked.connect(self.generate_clicked)
        self.reset_button.clicked.connect(self.clear)
        self.calc_iterations_button.clicked.connect(self.calc_clicked)

        control_layout.addWidget(self.generate_button)
        control_layout.addWidget(self.reset_button)
        control_layout.addWidget(self.calc_iterations_button)
        # ---------------------------------------------

        # -------------- slider control --------------
        slider_layout = QHBoxLayout()

        # Initialize the slider
        self.iterations_slider.setMinimum(0)
        self.iterations_slider.setMaximum(self.iterations)
        self.iterations_slider.setValue(0)  # Set initial value if needed
        self.iterations_slider.valueChanged.connect(self.slider_changed)
        slider_layout.addWidget(self.iterations_slider)
        self.iterations_slider.setEnabled(False)
        # ---------------------------------------------

        # add control buttons to main layout
        main_layout.addLayout(control_layout)

        # add slider to main layout
        main_layout.addLayout(slider_layout)

        self.setLayout(main_layout)
        self.setWindowTitle('Grid of Buttons')
        self.show()

    def button_clicked(self, button):
        # get button position
        position = button.property('position')
        button.setText('X') if button.text() == '' else button.setText('')
        # print button position
        print(f'Button at position {position} clicked!')

    def generate_clicked(self):
        self.clear()
        self.grid.fill_randomly()
        for row in range(self.m):
            for col in range(self.n):
                if self.grid.grid[row][col].state:
                    button = self.grid_layout.itemAtPosition(row, col).widget()
                    button.setStyleSheet('QPushButton {background-color: #FF0000}')
        self.grids = [self.grid]
        self.iterations_slider.setValue(0)
        self.iterations_slider.setDisabled(True)

    def clear(self):
        self.iterations_slider.setValue(0)
        self.grid = AutomataGrid(self.m, self.n)
        self.grids = [self.grid]
        for row in range(self.m):
            for col in range(self.n):
                button = self.grid_layout.itemAtPosition(row, col).widget()
                button.setStyleSheet('QPushButton {background-color: #FFFFFF}')
                button.setText('')
        self.iterations_slider.setDisabled(True)

    def calc_clicked(self):
        if self.grids[0].is_empty():
            return
        original = copy.deepcopy(self.grids[0])
        for i in range(self.iterations):
            self.grid.next_iteration()
            new_grid = copy.deepcopy(self.grid)
            self.grids.append(new_grid)
        self.grids[0] = original
        self.grid = original
        self.iterations_slider.setEnabled(True)

    def slider_changed(self, value):
        for row in range(self.m):
            for col in range(self.n):
                if self.grids[value].grid[row][col].state:
                    button = self.grid_layout.itemAtPosition(row, col).widget()
                    button.setStyleSheet('QPushButton {background-color: #FF0000}')
                else:
                    button = self.grid_layout.itemAtPosition(row, col).widget()
                    button.setStyleSheet('QPushButton {background-color: #FFFFFF}')
