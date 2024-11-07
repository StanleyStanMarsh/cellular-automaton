import sys
from PyQt6.QtWidgets import QApplication
from ui.choosewindow import ChooseWindow


def main():
    app = QApplication(sys.argv)
    choose_window = ChooseWindow()
    choose_window.show()
    app.exec()


if __name__ == '__main__':
    main()
