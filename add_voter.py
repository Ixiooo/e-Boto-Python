# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_voter.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery

import sqlite3

import images


class Ui_add_voter(object):

    def hideOnClick(self):
        add_voter.close()
    
    def add_voter(self):

        if(self.username.text()=="" or self.password.text()==""):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Add Voter")
            msg.setText("Error, please fill up forms properly")
            msg.exec_()
                                     
        else:
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName("database.db")
            db.open()

            username = self.username.text()
            password = self.password.text()

            qry= QSqlQuery()
            qry.prepare("INSERT INTO Voter (Username,Password) VALUES('"+username+"' , '"+password+"') ")
                
            if(qry.exec()):                
                db.commit()
                db.close()
                
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setWindowTitle("Add Voter")
                msg.setText("Voter Added Successfully")
                msg.exec_()

                self.username.clear()
                self.password.clear()
                
            else:                
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("Add Voter")
                msg.setText("Action Failed, Voter Already Exists")
                #msg.setText("Action Failed, Voter Already Exists"+qry.lastError().text())
                msg.exec_()
                db.close()
    
    def setupUi(self, add_voter):
        
        self.username = QtWidgets.QLineEdit(add_voter)
        self.username.setGeometry(QtCore.QRect(150, 60, 222, 37))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(10)
        self.username.setFont(font)
        self.username.setStyleSheet("background:0;")
        self.username.setObjectName("username")
        
        self.password = QtWidgets.QLineEdit(add_voter)
        self.password.setGeometry(QtCore.QRect(150, 120, 222, 37))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setStyleSheet("background:0;")
        self.password.setObjectName("password")

        add_voter.setObjectName("add_voter")
        add_voter.resize(400, 240)
        add_voter.setStyleSheet("background-image: url(:/Images/Dialog.png);")
        
        self.add = QtWidgets.QPushButton(add_voter)
        self.add.setGeometry(QtCore.QRect(70, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.add.setFont(font)
        self.add.setStyleSheet("background-image: url(:/Images/Button.png);\n"
"border-color: rgb(55, 113, 164);\n"
"color: rgb(255, 255, 255);")
        self.add.setAutoDefault(True)
        self.add.setDefault(False)
        self.add.setFlat(True)
        self.add.setObjectName("add")
                
        self.cancel = QtWidgets.QPushButton(add_voter)
        self.cancel.setGeometry(QtCore.QRect(200, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.cancel.setFont(font)
        self.cancel.setStyleSheet("background-image: url(:/Images/Button.png);\n"
"border-color: rgb(55, 113, 164);\n"
"color: rgb(255, 255, 255);")
        self.cancel.setAutoDefault(True)
        self.cancel.setDefault(False)
        self.cancel.setFlat(True)
        self.cancel.setObjectName("cancel")
        
        self.label = QtWidgets.QLabel(add_voter)
        self.label.setGeometry(QtCore.QRect(20, 65, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(add_voter)
        self.label_2.setGeometry(QtCore.QRect(20, 125, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(add_voter)
        QtCore.QMetaObject.connectSlotsByName(add_voter)
        

        
    
        ####Buttons
        
        self.cancel.clicked.connect(add_voter.close)
        self.add.clicked.connect(self.add_voter)

    
        
    def retranslateUi(self, add_voter):
        _translate = QtCore.QCoreApplication.translate
        add_voter.setWindowTitle(_translate("add_voter", "Add Voter"))
        
        self.add.setText(_translate("add_voter", "Add Voter"))
        self.cancel.setText(_translate("add_voter", "Cancel"))
        self.username.setPlaceholderText(_translate("add_voter", "Username"))
        self.password.setPlaceholderText(_translate("add_voter", "Password"))
        self.label.setText(_translate("add_voter", "<html><head/><body><p align=\"center\">Voter username</p></body></html>"))
        self.label_2.setText(_translate("add_voter", "<html><head/><body><p align=\"center\">Voter Password</p></body></html>"))


    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_voter = QtWidgets.QDialog()
    ui = Ui_add_voter()
    ui.setupUi(add_voter)
    add_voter.show()
    sys.exit(app.exec_())
