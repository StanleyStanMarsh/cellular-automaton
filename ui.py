from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton


class UIGrid(QWidget):
    def __init__(self, m, n):
        super().__init__()
        self.m = m
        self.n = n
        self.init_ui()

    def init_ui(self):
        # grid of buttons
        grid_layout = QGridLayout()

        # fill with QPushButton
        for row in range(self.m):
            for col in range(self.n):
                button = QPushButton('')
                minimize_coefficient = max(self.m / 2, self.n / 2)
                button.setFixedSize(int(250 / minimize_coefficient), int(250 / minimize_coefficient))
                # save button position
                button.setProperty('position', (row, col))
                # connect button click event with button_clicked()
                button.clicked.connect(lambda checked, b=button: self.button_clicked(b))
                grid_layout.addWidget(button, row, col)

            # Применяем сеточный компоновщик к виджету
        self.setLayout(grid_layout)
        self.setWindowTitle('Grid of Buttons')
        self.show()

    def button_clicked(self, button):
        # get button position
        position = button.property('position')
        button.setText('X') if button.text() == '' else button.setText('')
        # print button position
        print(f'Button at position {position} clicked!')
