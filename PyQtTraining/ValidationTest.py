import sys

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6.QtGui import QIntValidator
from ui_validationwindow import Ui_ValidationWindow
from ctrlVariables import StringVar, IntVar, DoubleVar
from PySide6.QtCore import Slot

class MainWindow(qtw.QMainWindow, Ui_ValidationWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.int1 = IntVar()
        self.int2 = IntVar()
        self.int3 = IntVar()


        self.pb_1.clicked.connect(self.vb_1)
        self.pb_2.clicked.connect(self.vb_2)
        self.pb_3.clicked.connect(self.vb_3)

        self.v1 = QIntValidator(1,15,self)
        self.le_1.setValidator(self.v1)

        self.v2 = QIntValidator(0,9,self)
        self.le_2.setValidator(self.v2)


        self.le_1.textEdited.connect(self.lb_f1.setText)
        # self.le_1.returnPressed.connect(self.hit)

    @Slot()
    def hit(self):
        print('Hit')

    @Slot()
    def moveTo2(self):
        print('Move to field 2')

    def vb_1(self):
        print('vb_1')
        # vb_1 action

    def vb_2(self):
        print('vb_2')
        # vb_2 action

    def vb_3(self):
        print('vb_3')
        # vb_3 action

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())