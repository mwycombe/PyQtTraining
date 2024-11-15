import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 Window')
        self.setWindowIcon(QIcon('qt.png'))
        # self.setFixedHeight(200)
        # self.setFixedWidth(200)
        self.setGeometry(500,300,400,300)
        self.setStyleSheet('background-color:orange')

app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())