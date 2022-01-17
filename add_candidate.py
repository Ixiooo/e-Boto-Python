# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_candidate.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

import images

class Ui_add_candidate(object):

    def add_voter(self):
        if(self.name.text()==""):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Add Candidate")
            msg.setText("Error, Please fill up forms properly")
            msg.exec_()
                                     
        else:
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName("database.db")
            db.open()

            name = self.name.text()
            position = self.position_combo.currentText()

            qry= QSqlQuery()
            qry.prepare("INSERT INTO Candidate (Name,Position) VALUES('"+name+"' , '"+position+"') ")
                
            if(qry.exec()):                
                db.commit()
                db.close()
                
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setWindowTitle("Add Candidate")
                msg.setText("Candidate Added Successfully")
                msg.exec_()
                
                self.name.clear()
                
            else:                
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("Add Candidate")
                msg.setText("Action Failed, Voter Already Exists")
                #msg.setText("Action Failed, Voter Already Exists"+qry.lastError().text())
                msg.exec_()
                db.close()
    
    def setupUi(self, add_candidate):
        
        add_candidate.setObjectName("add_candidate")
        add_candidate.resize(400, 240)
        add_candidate.setStyleSheet("background-image: url(:/Images/Dialog.png);")

        self.label = QtWidgets.QLabel(add_candidate)
        self.label.setGeometry(QtCore.QRect(20, 65, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.label.setObjectName("label")
        
        
        
        self.label_2 = QtWidgets.QLabel(add_candidate)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.label_2.setObjectName("label_2")
        
        self.name = QtWidgets.QLineEdit(add_candidate)
        self.name.setGeometry(QtCore.QRect(150, 60, 222, 37))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(10)
        self.name.setFont(font)
        self.name.setStyleSheet("background:0;")
        self.name.setObjectName("name")
        self.name.setStyleSheet("background-color: rgb(53, 84, 118);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")

        self.position_combo = QtWidgets.QComboBox(add_candidate)
        self.position_combo.setGeometry(QtCore.QRect(190, 120, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(10)
        self.position_combo.setFont(font)
        self.position_combo.setStyleSheet("")
        self.position_combo.setCurrentText("")
        self.position_combo.setObjectName("candidate_combo")
        self.position_combo.setStyleSheet("background-color: rgb(53, 84, 118);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")


        self.add = QtWidgets.QPushButton(add_candidate)
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
        
        self.cancel = QtWidgets.QPushButton(add_candidate)
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
        
        self.retranslateUi(add_candidate)
        QtCore.QMetaObject.connectSlotsByName(add_candidate)

        ###Load Positions

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database.db")
        db.open()

        position_model = QSqlQueryModel()
        qry= QSqlQuery()
        qry.prepare("select Position from Position")
        qry.exec()

        position_model.setQuery(qry)
        self.position_combo.setModel(position_model)

        db.close()

        ###Buttons

        self.cancel.clicked.connect(add_candidate.close)
        self.add.clicked.connect(self.add_voter)
        
        
    def retranslateUi(self, add_candidate):
        _translate = QtCore.QCoreApplication.translate
        add_candidate.setWindowTitle(_translate("add_candidate", "Add Candidate"))
        self.label.setText(_translate("add_candidate", "<html><head/><body><p align=\"center\">Candidate name</p></body></html>"))
        self.add.setText(_translate("add_candidate", "Add Candidate"))
        self.label_2.setText(_translate("add_candidate", "<html><head/><body><p align=\"center\">candidate position</p></body></html>"))
        self.name.setPlaceholderText(_translate("add_candidate", "Candidate Name"))
        self.cancel.setText(_translate("add_candidate", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_candidate = QtWidgets.QDialog()
    ui = Ui_add_candidate()
    ui.setupUi(add_candidate)
    add_candidate.show()
    sys.exit(app.exec_())
