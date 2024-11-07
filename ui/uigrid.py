from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout
from automata.automatagrid import AutomataGrid


class UIGrid(QWidget):
    def __init__(self, m: int, n: int):
        super().__init__()
        self.generate_button = QPushButton('Сгенерировать')
        self.reset_button = QPushButton('Очистить')
        self.next_button = QPushButton('Следующая итерация')
        self.grid_layout = QGridLayout()
        self.is_clickable = False
        self.m = m
        self.n = n
        self.grid = AutomataGrid(m, n)
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

        # control buttons
        control_layout = QHBoxLayout()

        self.generate_button.clicked.connect(self.generate_clicked)
        self.reset_button.clicked.connect(self.clear)
        self.next_button.clicked.connect(self.next_clicked)

        control_layout.addWidget(self.generate_button)
        control_layout.addWidget(self.reset_button)
        control_layout.addWidget(self.next_button)

        # add control buttons to main layout
        main_layout.addLayout(control_layout)

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

    def clear(self):
        self.grid = AutomataGrid(self.m, self.n)
        for row in range(self.m):
            for col in range(self.n):
                button = self.grid_layout.itemAtPosition(row, col).widget()
                button.setStyleSheet('QPushButton {background-color: #FFFFFF}')
                button.setText('')

    def next_clicked(self):
        self.grid.next_iteration()
        for row in range(self.m):
            for col in range(self.n):
                if self.grid.grid[row][col].state:
                    button = self.grid_layout.itemAtPosition(row, col).widget()
                    button.setStyleSheet('QPushButton {background-color: #FF0000}')
                else:
                    button = self.grid_layout.itemAtPosition(row, col).widget()
                    button.setStyleSheet('QPushButton {background-color: #FFFFFF}')
                    button.setText('')
