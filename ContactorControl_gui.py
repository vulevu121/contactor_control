# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ContactorControl_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QWidget {\n"
"    color: rgb(218, 218, 218);\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLabel {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(59, 56, 56);\n"
"    height: 40px;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    background-color: transparent;\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0px 10px 0px 10px;\n"
"    left: 10px;\n"
"}\n"
"\n"
"QStatusBar {\n"
"    background: black;\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane {\n"
"    background-color: transparent;\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: left;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: rgb(59, 56, 56);\n"
"    border: 1px solid gray;\n"
"    padding: 10px;\n"
"    min-width: 150px;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 rgb(59, 56, 56), stop: 0.4 rgb(100, 95, 95),\n"
"                                stop: 0.5 rgb(80, 75, 75), stop: 1.0 rgb(59, 56, 56));\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QStackedWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QRadioButton {\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: rgb(59, 56, 56);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(59, 56, 56);\n"
"    selection-background-color: lightgray;\n"
"\n"
"}\n"
"\n"
"QProgressBar{\n"
"    background-color: rgb(59, 56, 56);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    color: black;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 800, 79))
        self.label_3.setObjectName("label_3")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, 800, 70))
        self.titleLabel.setObjectName("titleLabel")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 200, 480))
        self.frame.setStyleSheet("QFrame{\n"
"    background-color: rgb(59, 56, 56);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(41, 105, 121, 271))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.startStopBtn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.startStopBtn.setFont(font)
        self.startStopBtn.setStyleSheet("background-color: rgb(118, 118, 113);")
        self.startStopBtn.setObjectName("startStopBtn")
        self.verticalLayout.addWidget(self.startStopBtn)
        self.openContactorBtn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.openContactorBtn.setFont(font)
        self.openContactorBtn.setStyleSheet("background-color: rgb(118, 118, 113);")
        self.openContactorBtn.setObjectName("openContactorBtn")
        self.verticalLayout.addWidget(self.openContactorBtn)
        self.closeContactorBtn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.closeContactorBtn.setFont(font)
        self.closeContactorBtn.setStyleSheet("background-color: rgb(118, 118, 113);")
        self.closeContactorBtn.setObjectName("closeContactorBtn")
        self.verticalLayout.addWidget(self.closeContactorBtn)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(230, 110, 541, 281))
        self.groupBox.setObjectName("groupBox")
        self.Intruction = QtWidgets.QLabel(self.groupBox)
        self.Intruction.setGeometry(QtCore.QRect(20, 170, 491, 91))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Intruction.setFont(font)
        self.Intruction.setObjectName("Intruction")
        self.widget1 = QtWidgets.QWidget(self.groupBox)
        self.widget1.setGeometry(QtCore.QRect(30, 30, 401, 142))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tbStatus_2 = QtWidgets.QLabel(self.widget1)
        self.tbStatus_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tbStatus_2.setObjectName("tbStatus_2")
        self.gridLayout.addWidget(self.tbStatus_2, 1, 0, 1, 1)
        self.tbStatusBox = QtWidgets.QLineEdit(self.widget1)
        self.tbStatusBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.tbStatusBox.setReadOnly(True)
        self.tbStatusBox.setObjectName("tbStatusBox")
        self.gridLayout.addWidget(self.tbStatusBox, 0, 1, 1, 1)
        self.MaxCellTempBox = QtWidgets.QLineEdit(self.widget1)
        self.MaxCellTempBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.MaxCellTempBox.setReadOnly(True)
        self.MaxCellTempBox.setObjectName("MaxCellTempBox")
        self.gridLayout.addWidget(self.MaxCellTempBox, 1, 1, 1, 1)
        self.tbStatus = QtWidgets.QLabel(self.widget1)
        self.tbStatus.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tbStatus.setObjectName("tbStatus")
        self.gridLayout.addWidget(self.tbStatus, 0, 0, 1, 1)
        self.HVCurrentBox = QtWidgets.QLineEdit(self.widget1)
        self.HVCurrentBox.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.HVCurrentBox.setReadOnly(True)
        self.HVCurrentBox.setObjectName("HVCurrentBox")
        self.gridLayout.addWidget(self.HVCurrentBox, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2.raise_()
        self.frame.raise_()
        self.label_3.raise_()
        self.titleLabel.raise_()
        self.groupBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/background/graphics/revero_800.png\"/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/titlebar/graphics/titlebar.png\"/></p></body></html>"))
        self.titleLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">BECM Contacter Control</p></body></html>"))
        self.startStopBtn.setText(_translate("MainWindow", "Start"))
        self.openContactorBtn.setText(_translate("MainWindow", "Open"))
        self.closeContactorBtn.setText(_translate("MainWindow", "Close"))
        self.groupBox.setTitle(_translate("MainWindow", "Battery Status"))
        self.Intruction.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Toggle Flashing switch to ON before START</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Toogle Flashing switch to OFF before STOP</span></p></body></html>"))
        self.tbStatus_2.setText(_translate("MainWindow", "Max Cell Temp"))
        self.tbStatusBox.setText(_translate("MainWindow", "Test"))
        self.MaxCellTempBox.setText(_translate("MainWindow", "Test"))
        self.tbStatus.setText(_translate("MainWindow", "TB Status"))
        self.HVCurrentBox.setText(_translate("MainWindow", "Test"))
        self.label.setText(_translate("MainWindow", "HV Current"))

import rdm_graphics_rc
