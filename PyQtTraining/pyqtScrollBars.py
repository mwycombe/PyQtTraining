from PySide6.QtWidgets import QMainWindow, QListWidget, QListWidgetItem, QScrollBar
from PySide6.QtWidgets import *
from PySide6 import QtCore, QtGui
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys

class Top(QMainWindow):
    def __init__(self):
        super().__init__()

        # set title
        self.setWindowTitle('PyQT Scrolling')
        # set geometry
        self.setGeometry(100,100,500,400)
        # calling method
        self.UiComponents()

        # show all widgets
        self.show()

    def UiComponents(self):

        # method for components

        # creating a QListWidget
        list_widget = QListWidget(self)
        list_widget.setGeometry(50,70,150,80)

        # items for the list widget
        item1 = QListWidgetItem("PyQt6 First Item")
        item2 = QListWidgetItem("PyQt6 Second Item")
        item3 = QListWidgetItem("PyQt6 Third Item")
        item4 = QListWidgetItem("PyQt6 Fourth Item")
        item5 = QListWidgetItem("PyQt6 Fifth Item")
        item6 = QListWidgetItem("PyQt6 Sixth Item")
        item7 = QListWidgetItem("PyQt6 Seventh Item")
        item8 = QListWidgetItem("PyQt6 Eighth Item")
        item9 = QListWidgetItem("PyQt6 Ninth Item")
        item10 = QListWidgetItem("PyQt6 Tenth Item")

        # add the items to the ListWidget
        list_widget.addItem(item1)
        list_widget.addItem(item2)
        list_widget.addItem(item3)
        list_widget.addItem(item4)
        list_widget.addItem(item5)
        list_widget.addItem(item6)
        list_widget.addItem(item7)
        list_widget.addItem(item8)
        list_widget.addItem(item9)
        list_widget.addItem(item10)

        # scroll bar
        # scroll_bar = QScrollBar(self)
        # scroll_bar.setStyleSheet('background : lightgreen;')
        #
        # list_widget.addScrollBarWidget(scroll_bar, Qt.AlignLeft)

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Top()

# start the app
sys.exit(App.exec())