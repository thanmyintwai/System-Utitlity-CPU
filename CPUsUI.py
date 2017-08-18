# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CPUsUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(549, 267)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.c1 = QtGui.QProgressBar(self.centralwidget)
        self.c1.setGeometry(QtCore.QRect(200, 20, 231, 21))
        self.c1.setProperty("value", 23)
        self.c1.setObjectName(_fromUtf8("c1"))
        self.c2 = QtGui.QProgressBar(self.centralwidget)
        self.c2.setGeometry(QtCore.QRect(200, 60, 231, 21))
        self.c2.setProperty("value", 24)
        self.c2.setObjectName(_fromUtf8("c2"))
        self.c3 = QtGui.QProgressBar(self.centralwidget)
        self.c3.setGeometry(QtCore.QRect(200, 100, 231, 21))
        self.c3.setProperty("value", 24)
        self.c3.setObjectName(_fromUtf8("c3"))
        self.c4 = QtGui.QProgressBar(self.centralwidget)
        self.c4.setGeometry(QtCore.QRect(200, 140, 231, 21))
        self.c4.setProperty("value", 24)
        self.c4.setObjectName(_fromUtf8("c4"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 68, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 60, 68, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 100, 68, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 140, 68, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.RAM = QtGui.QProgressBar(self.centralwidget)
        self.RAM.setGeometry(QtCore.QRect(200, 180, 231, 21))
        self.RAM.setProperty("value", 24)
        self.RAM.setObjectName(_fromUtf8("RAM"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 180, 68, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 549, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.c1.setFormat(_translate("MainWindow", "%p%", None))
        self.label.setText(_translate("MainWindow", "CPU 1", None))
        self.label_2.setText(_translate("MainWindow", "CPU 2", None))
        self.label_3.setText(_translate("MainWindow", "CPU 3", None))
        self.label_4.setText(_translate("MainWindow", "CPU 4", None))
        self.label_5.setText(_translate("MainWindow", "RAM", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

