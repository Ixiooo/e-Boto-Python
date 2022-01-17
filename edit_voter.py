# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_voter.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

import images

class Ui_edit_voter(object):

    def load_voter(self):
        
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database.db")
        db.open()

        voter_model = QSqlQueryModel()
        qry= QSqlQuery()
        qry.prepare("select Username from Voter")
        qry.exec()

        voter_model.setQuery(qry)
        self.voter_combo.setModel(voter_model)

        db.close()

    def display_details(self):
        
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database.db")
        db.open()

        username = self.voter_combo.currentText()
        qry= QSqlQuery()
        qry.prepare("select Username,Password from Voter where Username ='"+username+"'")
        
        if(qry.exec()):
            
            while(qry.next()):

                self.old_username.setText(str(qry.value(0)))
                
                self.old_password.setText(str(qry.value(1)))
        
        db.close()
        
    def edit_voter(self):

        if(self.new_username.text()=="" or self.new_password.text()==""):

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Edit Voter")
            msg.setText("Error, please fill up forms properly")
            msg.exec_()

        else:
            old_username = self.old_username.text()
            new_username = self.new_username.text()
            new_password = self.new_password.text()
        
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName("database.db")
            db.open()

            qry = QSqlQuery()
            qry.prepare("Update Voter SET Username=(:username),Password=(:password) where Username=(:old_username)")
            qry.bindValue(":username",new_username)
            qry.bindValue(":password",new_password)
            qry.bindValue(":old_username",old_username)

            if(qry.exec()):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setWindowTitle("Edit Voter")
                msg.setText("Voter Edited Successfully")
                msg.exec_()
                
                self.new_username.clear()
                self.new_password.clear()
                self.load_voter()
                
                
                db.commit()
                db.close()

            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("Edit Voter")
                msg.setText("Action Failed, Voter Already Exists")
                #msg.setText("Action Failed, "+qry.lastError().text())
                msg.exec_()
                db.close()
            
            
                
            
    
    def setupUi(self, edit_voter):
        
        edit_voter.setObjectName("edit_voter")
        edit_voter.resize(401, 260)
        edit_voter.setStyleSheet("background-image: url(:/Images/Dialog.png);")

        self.voter_combo = QtWidgets.QComboBox(edit_voter)
        self.voter_combo.setGeometry(QtCore.QRect(200, 11, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.voter_combo.setFont(font)
        self.voter_combo.setObjectName("voter_combo")
        self.voter_combo.setStyleSheet("background-color: rgb(53, 84, 118);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"")
        self.voter_combo.setStyleSheet("background-color: rgb(53, 84, 118);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")


        self.old_username = QtWidgets.QLabel(edit_voter)
        self.old_username.setGeometry(QtCore.QRect(170, 50, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(16)
        self.old_username.setFont(font)
        self.old_username.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.old_username.setObjectName("old_username")

        
        self.old_password = QtWidgets.QLabel(edit_voter)
        self.old_password.setGeometry(QtCore.QRect(170, 80, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(16)
        self.old_password.setFont(font)
        self.old_password.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.old_password.setObjectName("old_password")
        
        self.label = QtWidgets.QLabel(edit_voter)
        self.label.setGeometry(QtCore.QRect(10, 124, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.label.setObjectName("label")

        self.new_username = QtWidgets.QLineEdit(edit_voter)
        self.new_username.setGeometry(QtCore.QRect(160, 120, 222, 37))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(10)
        self.new_username.setFont(font)
        self.new_username.setStyleSheet("background:0;")
        self.new_username.setObjectName("new_username")
        self.new_username.setStyleSheet("background-color: rgb(53, 84, 118);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")

        self.new_password = QtWidgets.QLineEdit(edit_voter)
        self.new_password.setGeometry(QtCore.QRect(160, 170, 222, 37))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(10)
        self.new_password.setFont(font)
        self.new_password.setStyleSheet("background:0;")
        self.new_password.setObjectName("new_password")
        self.new_password.setStyleSheet("background-color: rgb(53, 84, 118);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        
        self.label_2 = QtWidgets.QLabel(edit_voter)
        self.label_2.setGeometry(QtCore.QRect(10, 173, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(edit_voter)
        self.label_3.setGeometry(QtCore.QRect(40, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(edit_voter)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(edit_voter)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.label_5.setObjectName("label_5")

        self.edit = QtWidgets.QPushButton(edit_voter)
        self.edit.setGeometry(QtCore.QRect(70, 220, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.edit.setFont(font)
        self.edit.setStyleSheet("background-image: url(:/Images/Button.png);\n"
"border-color: rgb(55, 113, 164);\n"
"color: rgb(255, 255, 255);")
        self.edit.setAutoDefault(True)
        self.edit.setDefault(False)
        self.edit.setFlat(True)
        self.edit.setObjectName("edit")
        
        self.cancel = QtWidgets.QPushButton(edit_voter)
        self.cancel.setGeometry(QtCore.QRect(200, 220, 111, 31))
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

        
        
        self.retranslateUi(edit_voter)
        QtCore.QMetaObject.connectSlotsByName(edit_voter)

        ###Load Data to Voter Combo Box
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database.db")
        db.open()

        voter_model = QSqlQueryModel()
        qry= QSqlQuery()
        qry.prepare("select Username from Voter")
        qry.exec()

        voter_model.setQuery(qry)
        self.voter_combo.setModel(voter_model)

        db.close()
        

        #####Data to Label
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database.db")
        db.open()

        username = self.voter_combo.currentText()
        qry= QSqlQuery()
        qry.prepare("select Username,Password from Voter where Username ='"+username+"'")
        
        if(qry.exec()):
            
            while(qry.next()):

                self.old_username.setText(str(qry.value(0)))
                
                self.old_password.setText(str(qry.value(1)))
        
        db.close()
        

        ####Buttons
        
        self.voter_combo.currentIndexChanged.connect(self.display_details)
        self.cancel.clicked.connect(edit_voter.close)
        self.edit.clicked.connect(self.edit_voter)
        
    def retranslateUi(self, edit_voter):
        _translate = QtCore.QCoreApplication.translate
        edit_voter.setWindowTitle(_translate("edit_voter", "Edit Voter"))
        self.cancel.setText(_translate("edit_voter", "Cancel"))
        self.label.setText(_translate("edit_voter", "<html><head/><body><p align=\"center\">NEW Voter username</p></body></html>"))
        self.edit.setText(_translate("edit_voter", "Edit Voter"))
        self.new_password.setPlaceholderText(_translate("edit_voter", "New Password"))
        self.new_username.setPlaceholderText(_translate("edit_voter", "New Username"))
        self.label_2.setText(_translate("edit_voter", "<html><head/><body><p align=\"center\">NEW Voter Password</p></body></html>"))
        self.label_3.setText(_translate("edit_voter", "<html><head/><body><p align=\"center\">SELECT VOTER TO EDIT</p></body></html>"))
        self.label_4.setText(_translate("edit_voter", "<html><head/><body><p align=\"center\">Old Voter username</p></body></html>"))
        self.label_5.setText(_translate("edit_voter", "<html><head/><body><p align=\"center\">Old Voter password</p></body></html>"))
        self.old_username.setText(_translate("edit_voter", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.old_password.setText(_translate("edit_voter", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    edit_voter = QtWidgets.QDialog()
    ui = Ui_edit_voter()
    ui.setupUi(edit_voter)
    edit_voter.show()
    sys.exit(app.exec_())
