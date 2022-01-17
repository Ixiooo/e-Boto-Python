# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_login.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

from admin_panel import Ui_admin_panel
import images

import sqlite3

class Ui_admin_login(object):

    def login(self):
        username = self.username_field.text()
        password = self.password_field.text()

        db = sqlite3.connect("database.db")
        query = db.execute("SELECT * FROM Admin WHERE Username =? AND PASSWORD = ?" ,(username,password))

        if(len(query.fetchall()) > 0):

            self.admin_panel = QtWidgets.QDialog()
            self.ui = Ui_admin_panel()
            self.ui.setupUi(self.admin_panel)

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle("Login")
            msg.setText("Login Successful")
            msg.exec_()
            
            admin_login.hide()
            self.admin_panel.show()
            db.close()
            
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Login")
            msg.setText("Login Failed, Check Your Credentials")
            msg.exec_()

            db.close()
            
    
    def setupUi(self, admin_login):
        admin_login.setObjectName("admin_login")
        admin_login.resize(360, 480)
        admin_login.setStyleSheet("image: url(:Images/Login Background Low.JPG);")
        
        self.label = QtWidgets.QLabel(admin_login)
        self.label.setGeometry(QtCore.QRect(0, 0, 361, 481))
        self.label.setStyleSheet("image: url(:/Images/Admin Login.PNG);")
        self.label.setText("")
        self.label.setObjectName("label")
        
        self.username_field = QtWidgets.QLineEdit(admin_login)
        self.username_field.setGeometry(QtCore.QRect(90, 212, 222, 37))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(10)
        self.username_field.setFont(font)
        self.username_field.setStyleSheet("background:0;")
        self.username_field.setObjectName("username_field")
        
        self.password_field = QtWidgets.QLineEdit(admin_login)
        self.password_field.setGeometry(QtCore.QRect(90, 270, 223, 37))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(10)
        self.password_field.setFont(font)
        self.password_field.setStyleSheet("background:0;\n"
"")
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_field.setObjectName("password_field")
        self.login_button = QtWidgets.QPushButton(admin_login)
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
        
        self.retranslateUi(admin_login)
        QtCore.QMetaObject.connectSlotsByName(admin_login)

        ######Buttons
        
        self.login_button.clicked.connect(self.login)
        
    def retranslateUi(self, admin_login):
        _translate = QtCore.QCoreApplication.translate
        admin_login.setWindowTitle(_translate("admin_login", "Admin Login"))
        self.username_field.setPlaceholderText(_translate("admin_login", "  Admin Username"))
        self.password_field.setPlaceholderText(_translate("admin_login", "  Admin Password"))
        self.login_button.setText(_translate("admin_login", "Login"))
        

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_login = QtWidgets.QDialog()
    ui = Ui_admin_login()
    ui.setupUi(admin_login)
    admin_login.show()
    sys.exit(app.exec_())
