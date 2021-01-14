# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'udp-reciever_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import asyncio
from threading import Thread

from PyQt5.QtCore import QRunnable, pyqtSlot, QThreadPool, QObject, QThread


class Worker(QObject):
    '''
    Worker thread
    '''

    def setAction(self,function):
        self.exec = function


    def run(self):
        self.exec()

class readProcess:
    def __init__(self, process, exec):
        self.p = process
        self.exec = exec
        self.t = Thread(target=self.executionStub)
        self.t.start()

    def executionStub(self):
        p = self.p
        while (True):
            line = p.readline()
            if (not line):
                break
            self.exec(line)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.flag=True
        Dialog.setObjectName("Dialog")
        Dialog.resize(567, 582)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(420, 370, 111, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 370, 271, 28))
        self.lineEdit.setObjectName("lineEdit")
        pwd = os.getcwd().replace(" ", "\ ")
        self.lineEdit.setText(pwd + "/recived/")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 369, 41, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 451, 271, 28))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText("5006")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 450, 41, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 510, 91, 41))
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.portOpener)
        #self.pushButton_2.clicked.connect(self.passSender)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(90, 110, 381, 192))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TCP Sender"))
        self.label.setText(_translate("Dialog", "TCP Reciever"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.label_2.setText(_translate("Dialog", "Dir:"))
        self.label_4.setText(_translate("Dialog", "Port:"))
        self.pushButton_2.setText(_translate("Dialog", "Recieve"))


    def runner(self):
        dirdata = self.lineEdit.text()
        if not dirdata:
            dirdata = "recived"
        if self.lineEdit_3.text() == "":
            port = 5006
        else:
            port = int(self.lineEdit_3.text())
        self.server = os.popen("python ncTCPServerFileTest.py -tp "+str(port)+" "+"--dir "+str(dirdata)+"&")
        exec = lambda data: self.textBrowser.setPlainText(self.textBrowser.toPlainText()+data)
        while (True):
            line = self.server.readline()
            if (not line):
                break
            exec(line)


    def portOpener(self):
        if self.flag:
            self.thread = QThread()
            self.worker = Worker()
            self.worker.setAction(self.runner)
            self.thread.started.connect(self.worker.run)
            self.thread.start()
            self.pushButton_2.setText("Close")
            self.flag=False
        else:
            exit(0)
        #self.runner()
        #worker = Worker()
        #worker.setAction(self.runner)
        #self.threadpool.start(worker)


        # serverReader  = readProcess(self.server,exec)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
