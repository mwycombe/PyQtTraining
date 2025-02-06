import sys
from PySide6.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem
from PySide6.QtCore import Signal,Slot

class ListWidgetDemo(QListWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)

        self.setStyleSheet('font-size: 35')

        jan = 'January'
        feb = 'February'
        mar = 'March'
        apr = 'April'
        may = 'May'
        jun = 'June'

        # add one item at a time
        # self.addItem(QListWidgetItem(jan))
        self.addItem(jan)
        self.addItem(feb)
        self.addItems([apr, jun])

        self.insertItem(2,mar)
        self.insertItem(4,may)

        self.itemSelectionChanged.connect(self.getCurrentRow)

    @Slot()
    def getCurrentRow(self):
        row = self.currentRow()
        print('Current Row: ', row)
        # move the focus
        self.setCurrentItem(self.item(row))
        print ('Current item: ', self.currentItem().text())
if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = ListWidgetDemo()
    demo.show()

    sys.exit(app.exec())