from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
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
            if 1 < m < 51 and 1 < n < 51 and iterations > 0:
                # Instantiate UIGrid
                self.ui_grid = UIGrid(m, n, iterations)
                self.ui_grid.show()
            else:
                msg = QMessageBox.critical(
                    self,
                    "Ошибка",
                    "Неверный ввод. Пожалуйста, введите значения "
                    "от 2 до 51 для размера поля и от 1 до 200 для числа итераций."
                )
        except ValueError:
            msg = QMessageBox.critical(
                self,
                "Ошибка",
                "Неверный ввод. Пожалуйста, введите числовые значения."
            )
