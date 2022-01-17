# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_candidate.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

import images

class Ui_delete_candidate(object):

    def load_cand(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database.db")
        db.open()

        candidate_model = QSqlQueryModel()
        qry= QSqlQuery()
        candidate_model.setQuery("select Name from Candidate where Position ='"+self.position_combo.currentText()+"' ")

        self.name_combo.setModel(candidate_model)

        db.close()

    def delete_candidate(self):
        
        if(self.name_combo.currentText()==""):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Delete Candidate")
            msg.setText("Error, Please Select Candidate to Delete")
            msg.exec_()
        else:           
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Question)
            msg.setWindowTitle("Delete Candidate")
            msg.setText("Are You Sure You Want to Delete this Candidate?")
            msg.setStandardButtons(QMessageBox.Yes| QMessageBox.No  )
            msg.setDefaultButton(QMessageBox.No)
            answer = msg.exec_()

            if answer == QMessageBox.Yes:
   
                db = QSqlDatabase.addDatabase("QSQLITE")
                db.setDatabaseName("database.db")
                db.open()

                name = self.name_combo.currentText()
                qry = QSqlQuery()

                qry.prepare("DELETE FROM Candidate WHERE Name= '"+name+"' ")

                if(qry.exec()):
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Information)
                    msg.setWindowTitle("Delete Candidate")
                    msg.setText("Candidate Deleted Successfully")
                    msg.exec_()
                    
                    self.load_cand()
                    
                    db.commit()
                    db.close()
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.setWindowTitle("Delete Candidate")
                    #msg.setText("Action Failed, Voter Already Exists")
                    msg.setText("Action Failed, "+qry.lastError().text())
                    msg.exec_()
                    db.close()
                    
            elif answer == QMessageBox.No:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setWindowTitle("Delete Candidate")
                msg.setText("Candidate Not Deleted")
                #msg.setText("Action Failed, "+qry.lastError().text())
                msg.exec_()
    
    
    def setupUi(self, delete_candidate):
        
        delete_candidate.setObjectName("delete_candidate")
        delete_candidate.resize(400, 240)
        delete_candidate.setStyleSheet("background-image: url(:/Images/Dialog.png);")

        self.position_combo = QtWidgets.QComboBox(delete_candidate)
        self.position_combo.setGeometry(QtCore.QRect(170, 80, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(10)
        self.position_combo.setFont(font)
        self.position_combo.setStyleSheet("background-color: rgb(53, 84, 118);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.position_combo.setObjectName("position_combo")

        self.name_combo = QtWidgets.QComboBox(delete_candidate)
        self.name_combo.setGeometry(QtCore.QRect(170, 130, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(10)
        self.name_combo.setFont(font)
        self.name_combo.setStyleSheet("background-color: rgb(53, 84, 118);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.name_combo.setObjectName("name_combo")
        
        self.delete_2 = QtWidgets.QPushButton(delete_candidate)
        self.delete_2.setGeometry(QtCore.QRect(70, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.delete_2.setFont(font)
        self.delete_2.setStyleSheet("background-image: url(:/Images/Button.png);\n"
"border-color: rgb(55, 113, 164);\n"
"color: rgb(255, 255, 255);")
        self.delete_2.setAutoDefault(True)
        self.delete_2.setDefault(False)
        self.delete_2.setFlat(True)
        self.delete_2.setObjectName("delete_2")
        
        self.cancel = QtWidgets.QPushButton(delete_candidate)
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
        
        self.label = QtWidgets.QLabel(delete_candidate)
        self.label.setGeometry(QtCore.QRect(80, 40, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.label.setObjectName("label")

        self.label_4 = QtWidgets.QLabel(delete_candidate)
        self.label_4.setGeometry(QtCore.QRect(30, 80, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(delete_candidate)
        self.label_5.setGeometry(QtCore.QRect(30, 130, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(delete_candidate)
        QtCore.QMetaObject.connectSlotsByName(delete_candidate)
        delete_candidate.setTabOrder(self.position_combo, self.name_combo)
        delete_candidate.setTabOrder(self.name_combo, self.delete_2)
        delete_candidate.setTabOrder(self.delete_2, self.cancel)

        ###Load Positions to Combo Box

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database.db")
        db.open()

        position_model = QSqlQueryModel()
        qry= QSqlQuery()
        qry.prepare("select Position from Position")
        qry.exec()

        position_model.setQuery(qry)
        
        self.position_combo.setModel(position_model)    #Position
        db.close()
        
        ###Display Candidate to Combo Box
        
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database.db")
        db.open()

        candidate_model = QSqlQueryModel()
        qry= QSqlQuery()
        candidate_model.setQuery("select Name from Candidate where Position ='"+self.position_combo.currentText()+"' ")

        self.name_combo.setModel(candidate_model)

        db.close()

        ###Buttons
        self.cancel.clicked.connect(delete_candidate.close)
        self.delete_2.clicked.connect(self.delete_candidate)
        self.position_combo.currentIndexChanged.connect(self.load_cand)

        
    def retranslateUi(self, delete_candidate):
        _translate = QtCore.QCoreApplication.translate
        delete_candidate.setWindowTitle(_translate("delete_candidate", "Delete Candidate"))
        self.delete_2.setText(_translate("delete_candidate", "Delete Candidate"))
        self.cancel.setText(_translate("delete_candidate", "Cancel"))
        self.label.setText(_translate("delete_candidate", "<html><head/><body><p align=\"center\">select candidate to delete</p></body></html>"))
        self.label_4.setText(_translate("edit_candidate", "<html><head/><body><p align=\"center\">Position</p></body></html>"))
        self.label_5.setText(_translate("edit_candidate", "<html><head/><body><p align=\"center\">Name</p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    delete_candidate = QtWidgets.QDialog()
    ui = Ui_delete_candidate()
    ui.setupUi(delete_candidate)
    delete_candidate.show()
    sys.exit(app.exec_())
