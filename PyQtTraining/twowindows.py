import sys

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6.QtWidgets import QApplication

from SS_form_1 import Ui_SS_form_1
from SS_form_2 import Ui_SS_form_2

class form1(qtw.QWidget, Ui_SS_form_1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_changeText.clicked.connect(self.button_change_text)

    @qtc.Slot()
    def showChangedText(self,t):
        self.lb_changedText.setText(t)


    @qtc.Slot()
    def button_change_text(self):
        self.form2 = form2()
        self.form2.setupUi(self.form2)
        # print ('instantiate form2')
        self.form2.submitted.connect(self.lb_changedText.setText)
        self.form2.show()
        # print ('button-changed-text')


class form2(qtw.QWidget, Ui_SS_form_2):

    submitted = qtc.Signal(str)

    def __init_(self):
        super().__init__()
        self.setupUi(self)
        self.pb_submitText.clicked.connect(self.button_submit)

    def button_submit(self):
        print ('submit text pressed')
        self.submitted.emit(self.le_inputText.text())
        self.close()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = form1()
    window.show()

    sys.exit(app.exec())