import sys
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")

if __name__ == '__main__':
    # Create QT application
    app = QApplication(sys.argv)
    # Create and whow the form
    form = Form()
    form.show()
    #Run the main Qt loop
    sys.exit(app.exec())

