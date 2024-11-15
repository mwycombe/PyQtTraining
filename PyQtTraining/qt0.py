import sys
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
from PySide6 import QtWidgets as qtw

from PySide6.QtWidgets import QApplication, QWidget

sys.path.append('E:\Pycharm\CribbageQt\CribbageQt')
sys.path.append("E:\Pycharm\CribbageQt\CribbageQt\\UI")

print (sys.path)

import masterscreenV3

app = QApplication(sys.argv)

window = QWidget()
window.show()

sys.exit(app.exec())