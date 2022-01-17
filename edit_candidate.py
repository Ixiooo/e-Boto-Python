# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_candidate.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

import images


class Ui_edit_candidate(object):

    def load_name(self):

        currentPosition=self.old_position_combo.currentText()
        
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database.db")
        db.open()

        load_model = QSqlQueryModel()
        load_model.setQuery("select Name from Candidate where Position ='"+currentPosition+"' ")

        self.old_name_combo.setModel(load_model)

        db.close()


        
    def edit_candidate(self):
        if(self.position_combo.currentText()=="" or self.new_name.text()==""):

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Edit Candidate")
            msg.setText("Error, please fill up forms properly")
            msg.exec_()

        else:
            current_name = self.old_name_combo.currentText()
            new_name = self.new_name.text()
            new_position = self.position_combo.currentText()
        
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName("database.db")
            db.open()

            qry = QSqlQuery()
            qry.prepare("Update Candidate SET Name=(:new_name),Position=(:new_position) where Name=(:current_name)")
            qry.bindValue(":new_name",new_name)
            qry.bindValue(":new_position",new_position)
            qry.bindValue(":current_name",current_name)

            if(qry.exec()):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setWindowTitle("Edit Candidate")
                msg.setText("Candidate Edited Successfully")
                msg.exec_()

                self.load_name()
                self.new_name.clear()

                db.commit()
                db.close()

            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("Edit Candidate")
                msg.setText("Action Failed, Voter Already Exists")
                #msg.setText("Action Failed, "+qry.lastError().text())
                msg.exec_()
                db.close()

    
    def setupUi(self, edit_candidate):

        
        edit_candidate.setObjectName("edit_candidate")
        edit_candidate.resize(400, 300)
        edit_candidate.setStyleSheet("background-image: url(:/Images/Dialog.png);")


        self.label_2 = QtWidgets.QLabel(edit_candidate)
        self.label_2.setGeometry(QtCore.QRect(50, 220, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.label_2.setObjectName("label_2")
        
        self.old_position_combo = QtWidgets.QComboBox(edit_candidate)
        self.old_position_combo.setGeometry(QtCore.QRect(190, 70, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(10)
        self.old_position_combo.setFont(font)
        self.old_position_combo.setStyleSheet("")
        self.old_position_combo.setObjectName("old_position_combo")
        self.old_position_combo.setStyleSheet("background-color: rgb(53, 84, 118);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")

        
        self.label_3 = QtWidgets.QLabel(edit_candidate)
        self.label_3.setGeometry(QtCore.QRect(90, 10, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(edit_candidate)
        self.label_4.setGeometry(QtCore.QRect(50, 120, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(edit_candidate)
        self.label_5.setGeometry(QtCore.QRect(30, 70, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(edit_candidate)
        self.label.setGeometry(QtCore.QRect(60, 170, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.old_name_combo = QtWidgets.QComboBox(edit_candidate)
        self.old_name_combo.setGeometry(QtCore.QRect(190, 120, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(10)
        self.old_name_combo.setFont(font)
        self.old_name_combo.setStyleSheet("")
        self.old_name_combo.setObjectName("old_name_combo")
        self.old_name_combo.setStyleSheet("background-color: rgb(53, 84, 118);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        
        self.label.setObjectName("label")
        self.new_name = QtWidgets.QLineEdit(edit_candidate)
        self.new_name.setGeometry(QtCore.QRect(190, 170, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(10)
        self.new_name.setFont(font)
        self.new_name.setStyleSheet("background:0;")
        self.new_name.setObjectName("new_name")
        self.new_name.setStyleSheet("background-color: rgb(53, 84, 118);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        
        self.position_combo = QtWidgets.QComboBox(edit_candidate)
        self.position_combo.setGeometry(QtCore.QRect(190, 220, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(10)
        self.position_combo.setFont(font)
        self.position_combo.setStyleSheet("")
        self.position_combo.setCurrentText("")
        self.position_combo.setObjectName("position_combo")
        self.position_combo.setStyleSheet("background-color: rgb(53, 84, 118);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        

        self.edit = QtWidgets.QPushButton(edit_candidate)
        self.edit.setGeometry(QtCore.QRect(80, 260, 111, 31))
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
        
        self.cancel = QtWidgets.QPushButton(edit_candidate)
        self.cancel.setGeometry(QtCore.QRect(210, 260, 111, 31))
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

                
        self.retranslateUi(edit_candidate)
        QtCore.QMetaObject.connectSlotsByName(edit_candidate)


        ###Load Positions to Combo Box

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database.db")
        db.open()

        position_model = QSqlQueryModel()
        qry= QSqlQuery()
        qry.prepare("select Position from Position")
        qry.exec()

        position_model.setQuery(qry)
        
        self.position_combo.setModel(position_model)    #New Position
        self.old_position_combo.setModel(position_model)    #Current Position
        db.close()
        
        #####Load Current Name to Combo Box
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database.db")
        db.open()

        currentPosition=self.old_position_combo.currentText()
        
        name_model = QSqlQueryModel()
        qry= QSqlQuery()
        qry.prepare("select Name from Candidate where Position ='"+currentPosition+"' ")
        qry.exec()

        name_model.setQuery(qry)
        self.old_name_combo.setModel(name_model)

        db.close()

        
        

        ###Buttons

        self.old_position_combo.currentIndexChanged.connect(self.load_name)
        self.edit.clicked.connect(self.edit_candidate)
        self.cancel.clicked.connect(edit_candidate.close)
        

    def retranslateUi(self, edit_candidate):
        _translate = QtCore.QCoreApplication.translate
        edit_candidate.setWindowTitle(_translate("edit_candidate", "Edit Candidate"))
        self.label_2.setText(_translate("edit_candidate", "<html><head/><body><p align=\"center\">NEW position</p></body></html>"))
        self.edit.setText(_translate("edit_candidate", "Edit Candidate"))
        self.label_3.setText(_translate("edit_candidate", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">SELECT candidate TO EDIT</span></p></body></html>"))
        self.label_4.setText(_translate("edit_candidate", "<html><head/><body><p align=\"center\">current name</p></body></html>"))
        self.cancel.setText(_translate("edit_candidate", "Cancel"))
        self.label_5.setText(_translate("edit_candidate", "<html><head/><body><p align=\"center\">current position</p></body></html>"))
        self.label.setText(_translate("edit_candidate", "<html><head/><body><p align=\"center\">NEW name</p></body></html>"))
        self.new_name.setPlaceholderText(_translate("edit_candidate", "New Candidate Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    edit_candidate = QtWidgets.QDialog()
    ui = Ui_edit_candidate()
    ui.setupUi(edit_candidate)
    edit_candidate.show()
    sys.exit(app.exec_())
