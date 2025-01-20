# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'validationwindowUGhtPJ.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_ValidationWindow(object):
    def setupUi(self, ValidationWindow):
        if not ValidationWindow.objectName():
            ValidationWindow.setObjectName(u"ValidationWindow")
        ValidationWindow.resize(800, 600)
        self.centralwidget = QWidget(ValidationWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(90, 40, 97, 151))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_1 = QLabel(self.widget)
        self.lb_1.setObjectName(u"lb_1")

        self.verticalLayout.addWidget(self.lb_1)

        self.lb_2 = QLabel(self.widget)
        self.lb_2.setObjectName(u"lb_2")

        self.verticalLayout.addWidget(self.lb_2)

        self.lb_3 = QLabel(self.widget)
        self.lb_3.setObjectName(u"lb_3")

        self.verticalLayout.addWidget(self.lb_3)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(100, 260, 91, 141))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pb_1 = QPushButton(self.widget1)
        self.pb_1.setObjectName(u"pb_1")

        self.verticalLayout_2.addWidget(self.pb_1)

        self.pb_2 = QPushButton(self.widget1)
        self.pb_2.setObjectName(u"pb_2")

        self.verticalLayout_2.addWidget(self.pb_2)

        self.pb_3 = QPushButton(self.widget1)
        self.pb_3.setObjectName(u"pb_3")

        self.verticalLayout_2.addWidget(self.pb_3)

        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(230, 40, 152, 151))
        self.verticalLayout_3 = QVBoxLayout(self.widget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.le_1 = QLineEdit(self.widget2)
        self.le_1.setObjectName(u"le_1")

        self.verticalLayout_3.addWidget(self.le_1)

        self.le_2 = QLineEdit(self.widget2)
        self.le_2.setObjectName(u"le_2")

        self.verticalLayout_3.addWidget(self.le_2)

        self.le_3 = QLineEdit(self.widget2)
        self.le_3.setObjectName(u"le_3")

        self.verticalLayout_3.addWidget(self.le_3)

        ValidationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ValidationWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        ValidationWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ValidationWindow)
        self.statusbar.setObjectName(u"statusbar")
        ValidationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ValidationWindow)

        QMetaObject.connectSlotsByName(ValidationWindow)
    # setupUi

    def retranslateUi(self, ValidationWindow):
        ValidationWindow.setWindowTitle(QCoreApplication.translate("ValidationWindow", u"Validation Window", None))
        self.lb_1.setText(QCoreApplication.translate("ValidationWindow", u"Integer Field 1", None))
        self.lb_2.setText(QCoreApplication.translate("ValidationWindow", u"Integer Field 2", None))
        self.lb_3.setText(QCoreApplication.translate("ValidationWindow", u"Integer Field 3", None))
        self.pb_1.setText(QCoreApplication.translate("ValidationWindow", u"Validate 1", None))
        self.pb_2.setText(QCoreApplication.translate("ValidationWindow", u"Validate 2", None))
        self.pb_3.setText(QCoreApplication.translate("ValidationWindow", u"Validate 3", None))
    # retranslateUi

