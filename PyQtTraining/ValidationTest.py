import sys

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6.QtGui import QIntValidator
from ui_validationwindow import Ui_ValidationWindow

class MainWindow(qtw.QMainWindow, Ui_ValidationWindow):
    def __init__(self):
        super().__init__()
        self.show()



if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())