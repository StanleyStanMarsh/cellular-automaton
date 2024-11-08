from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QApplication
from ui.uigrid import UIGrid


class ChooseWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.m_input = QLineEdit(self)
        self.n_input = QLineEdit(self)
        self.iterations_input = QLineEdit(self)
        # Setting up the layout
        layout = QVBoxLayout()

        # Adding inputs for grid size
        grid_size_layout = QHBoxLayout()
        grid_size_layout.addWidget(QLabel("Количество строк: "))
        grid_size_layout.addWidget(self.m_input)
        grid_size_layout.addWidget(QLabel("Количество столбцов: "))
        grid_size_layout.addWidget(self.n_input)
        layout.addLayout(grid_size_layout)

        # Adding input for iterations
        iterations_layout = QHBoxLayout()
        iterations_layout.addWidget(QLabel("Число итераций: "))
        iterations_layout.addWidget(self.iterations_input)
        layout.addLayout(iterations_layout)

        # Add confirm button to create UIGrid
        self.confirm_button = QPushButton("Создать поле", self)
        self.confirm_button.clicked.connect(self.create_grid)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)
        self.setWindowTitle("Выбор параметров поля")

    def create_grid(self):
        # Retrieve the input values
        try:
            m = int(self.m_input.text())
            n = int(self.n_input.text())
            iterations = int(self.iterations_input.text())

            # You can add validation checks here if needed
            if m > 1 and n > 1 and iterations > 0:
                # Instantiate UIGrid
                self.ui_grid = UIGrid(m, n, iterations)
                self.ui_grid.show()
            else:
                print("Invalid input values. Please enter values higher than 1.")
        except ValueError:
            print("Please enter valid integer values for grid size and iterations.")