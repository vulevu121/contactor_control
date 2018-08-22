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
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(230, 190, 141, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.startBtn.setFont(font)
        self.startBtn.setStyleSheet("background-color: rgb(118, 118, 113);")
        self.startBtn.setObjectName("startBtn")
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setGeometry(QtCore.QRect(420, 190, 141, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.stopBtn.setFont(font)
        self.stopBtn.setObjectName("stopBtn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 800, 79))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 800, 70))
        self.label_4.setObjectName("label_4")
        self.openContactorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openContactorBtn.setGeometry(QtCore.QRect(230, 320, 141, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.openContactorBtn.setFont(font)
        self.openContactorBtn.setStyleSheet("background-color: rgb(118, 118, 113);")
        self.openContactorBtn.setObjectName("openContactorBtn")
        self.closeContactorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.closeContactorBtn.setGeometry(QtCore.QRect(430, 320, 141, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.closeContactorBtn.setFont(font)
        self.closeContactorBtn.setStyleSheet("background-color: rgb(118, 118, 113);")
        self.closeContactorBtn.setObjectName("closeContactorBtn")
        self.Intruction = QtWidgets.QLabel(self.centralwidget)
        self.Intruction.setGeometry(QtCore.QRect(230, 70, 351, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Intruction.setFont(font)
        self.Intruction.setObjectName("Intruction")
        self.label_2.raise_()
        self.label_3.raise_()
        self.startBtn.raise_()
        self.stopBtn.raise_()
        self.label_4.raise_()
        self.openContactorBtn.raise_()
        self.closeContactorBtn.raise_()
        self.Intruction.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startBtn.setText(_translate("MainWindow", "Start"))
        self.stopBtn.setText(_translate("MainWindow", "Stop"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/background/graphics/revero_800.png\"/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/titlebar/graphics/titlebar.png\"/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">BECM Contacter Control</p></body></html>"))
        self.openContactorBtn.setText(_translate("MainWindow", "Open"))
        self.closeContactorBtn.setText(_translate("MainWindow", "Close"))
        self.Intruction.setText(_translate("MainWindow", "<html><head/><body><p>Toggle Flashing switch to ON before START</p><p>Toogle Flashing switch to OFF before STOP</p></body></html>"))

import rdm_graphics_rc
