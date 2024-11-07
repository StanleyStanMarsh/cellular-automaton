import copy
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout, QSlider, QComboBox
from automata.automatagrid import AutomataGrid


class UIGrid(QWidget):
    def __init__(self, m: int = 2, n: int = 2, iterations: int = 1):
        super().__init__()
        self.generate_button = QPushButton('Сгенерировать')
        self.reset_button = QPushButton('Очистить')
        self.calc_iterations_button = QPushButton('Просчитать итерации')
        self.input_choose_box = QComboBox()
        self.iterations_slider = QSlider(Qt.Orientation.Horizontal)
        self.grid_layout = QGridLayout()
        self.is_clickable = False
        self.rows = m
        self.columns = n
        self.iterations = iterations
        self.grid = AutomataGrid(m, n)
        self.grids = [self.grid]
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        # grid of buttons
        self.grid_layout = QGridLayout()

        # fill with QPushButton
        for row in range(self.rows):
            for col in range(self.columns):
                button = QPushButton('')
                minimize_coefficient = max(self.rows / 2, self.columns / 2)
                button.setFixedSize(int(250 / minimize_coefficient), int(250 / minimize_coefficient))
                button.setStyleSheet('QPushButton {background-color: #FFFFFF}')
                # button.setEnabled(self.is_clickable)
                # save button position
                button.setProperty('position', (row, col))
                # connect button click event with button_clicked()
                button.clicked.connect(lambda checked, b=button: self.button_clicked(b))
                self.grid_layout.addWidget(button, row, col)

        # add grid to main layout
        main_layout.addLayout(self.grid_layout)

        # -------------- control buttons --------------
        control_layout = QHBoxLayout()

        self.input_choose_box.addItems(['Вручную', 'Случайно'])
        self.input_choose_box.setCurrentIndex(0)
        self.input_choose_box.activated.connect(self.change_choose)

        self.generate_button.clicked.connect(self.generate_clicked)
        self.generate_button.setEnabled(False)

        self.reset_button.clicked.connect(self.clear)
        self.calc_iterations_button.clicked.connect(self.calc_clicked)

        control_layout.addWidget(self.generate_button)
        control_layout.addWidget(self.reset_button)
        control_layout.addWidget(self.calc_iterations_button)
        control_layout.addWidget(self.input_choose_box)
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
        # invert state
        position = button.property('position')
        row, col = position
        if self.grid.get_state(row, col):
            button.setStyleSheet('QPushButton {background-color: #FFFFFF}')
            self.grid.set_state(row, col, False)
            return

        button.setStyleSheet('QPushButton {background-color: #FF0000}')
        self.grid.set_state(row, col, True)

    def generate_clicked(self):
        self.clear()
        self.grid.fill_randomly()
        for row in range(self.rows):
            for col in range(self.columns):
                if self.grid.get_state(row, col):
                    button = self.grid_layout.itemAtPosition(row, col).widget()
                    button.setStyleSheet('QPushButton {background-color: #FF0000}')
        self.grids = [self.grid]
        self.iterations_slider.setValue(0)
        self.iterations_slider.setDisabled(True)

    def clear(self):
        self.iterations_slider.setValue(0)
        self.grid = AutomataGrid(self.rows, self.columns)
        self.grids = [self.grid]
        for row in range(self.rows):
            for col in range(self.columns):
                button = self.grid_layout.itemAtPosition(row, col).widget()
                button.setStyleSheet('QPushButton {background-color: #FFFFFF}')
                method = self.input_choose_box.currentIndex()
                match method:
                    case 0:
                        button.setEnabled(True)
                    case 1:
                        button.setEnabled(False)

        self.iterations_slider.setDisabled(True)

    def calc_clicked(self):
        # disable cells
        for row in range(self.rows):
            for col in range(self.columns):
                button = self.grid_layout.itemAtPosition(row, col).widget()
                button.setEnabled(False)

        original = copy.deepcopy(self.grids[0])
        for i in range(self.iterations):
            self.grid.next_iteration()
            new_grid = copy.deepcopy(self.grid)
            self.grids.append(new_grid)
        self.grids[0] = original
        self.grid = original
        self.iterations_slider.setEnabled(True)

    def slider_changed(self, value):
        for row in range(self.rows):
            for col in range(self.columns):
                if self.grids[value].get_state(row, col):
                    button = self.grid_layout.itemAtPosition(row, col).widget()
                    button.setStyleSheet('QPushButton {background-color: #FF0000}')
                else:
                    button = self.grid_layout.itemAtPosition(row, col).widget()
                    button.setStyleSheet('QPushButton {background-color: #FFFFFF}')

    def change_choose(self, index):
        match index:
            case 0:
                self.clear()
                self.generate_button.setEnabled(False)
                for row in range(self.rows):
                    for col in range(self.columns):
                        button = self.grid_layout.itemAtPosition(row, col).widget()
                        button.setEnabled(True)
            case 1:
                self.clear()
                self.generate_button.setEnabled(True)
                for row in range(self.rows):
                    for col in range(self.columns):
                        button = self.grid_layout.itemAtPosition(row, col).widget()
                        button.setEnabled(False)

