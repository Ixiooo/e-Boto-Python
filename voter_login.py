# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'voter_login.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

from voter_panel import Ui_voter_panel

import sqlite3


class Ui_voter_login(object):

    def login(self):
        username = self.username_field.text()
        password = self.password_field.text()

        db = sqlite3.connect("database.db")
        query = db.execute("SELECT * FROM Voter WHERE Username =? AND PASSWORD = ?" ,(username,password))

        if(len(query.fetchall()) > 0):

            self.voter_panel = QtWidgets.QDialog()
            self.ui = Ui_voter_panel()
            self.ui.setupUi(self.voter_panel)

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle("Login")
            msg.setText("Login Successful")
            msg.exec_()
            
            voter_login.hide()
            self.voter_panel.show()
            db.close()
            
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Login")
            msg.setText("Login Failed, Check Your Credentials")
            msg.exec_()

            db.close()


    
    def setupUi(self, voter_login):

        
        voter_login.setObjectName("voter_login")
        voter_login.resize(360, 480)

        
        self.username_field = QtWidgets.QLineEdit(voter_login)
        self.username_field.setGeometry(QtCore.QRect(90, 212, 222, 37))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(10)
        self.username_field.setFont(font)
        self.username_field.setStyleSheet("background:0;")
        self.username_field.setObjectName("username_field")

        
        self.label = QtWidgets.QLabel(voter_login)
        self.label.setGeometry(QtCore.QRect(0, 0, 361, 481))
        self.label.setStyleSheet("image: url(:/Images/Voter Login.PNG);")
        self.label.setText("")
        self.label.setObjectName("label")

        
        self.login_button = QtWidgets.QPushButton(voter_login)
        self.login_button.setGeometry(QtCore.QRect(53, 316, 260, 34))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(13)
        self.login_button.setFont(font)
        self.login_button.setFlat(True)
        self.login_button.setObjectName("login_button")

        
        self.password_field = QtWidgets.QLineEdit(voter_login)
        self.password_field.setGeometry(QtCore.QRect(90, 270, 223, 37))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(10)
        self.password_field.setFont(font)
        self.password_field.setStyleSheet("background:0;\n"
"")
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_field.setObjectName("password_field")
        self.label.raise_()
        self.username_field.raise_()
        self.login_button.raise_()
        self.password_field.raise_()

        self.retranslateUi(voter_login)
        QtCore.QMetaObject.connectSlotsByName(voter_login)
        self.password_field.setTabOrder(self.password_field, self.login_button)
        
        
        #####Buttons

        self.login_button.clicked.connect(self.login)
        
        
    def retranslateUi(self, voter_login):
        _translate = QtCore.QCoreApplication.translate
        voter_login.setWindowTitle(_translate("voter_login", "Voter Login"))
        self.username_field.setPlaceholderText(_translate("voter_login", "Voter Username"))
        self.login_button.setText(_translate("voter_login", "Login"))
        self.password_field.setPlaceholderText(_translate("voter_login", "Voter Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    voter_login = QtWidgets.QDialog()
    ui = Ui_voter_login()
    ui.setupUi(voter_login)
    voter_login.show()
    sys.exit(app.exec_())
