# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_voter.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

import images

class Ui_delete_voter(object):

    def delete_voter(self):

        if(self.voter_combo.currentText()==""):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Delete Voter")
            msg.setText("Error, Please select voter to delete")
            msg.exec_()
        else:
            
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Question)
            msg.setWindowTitle("Delete Voter")
            msg.setText("Are You Sure You Want to Delete this Voter?")
            msg.setStandardButtons(QMessageBox.Yes| QMessageBox.No  )
            msg.setDefaultButton(QMessageBox.No)
            answer = msg.exec_()

            if answer == QMessageBox.Yes:
   
                db = QSqlDatabase.addDatabase("QSQLITE")
                db.setDatabaseName("database.db")
                db.open()

                username = self.voter_combo.currentText()
                qry = QSqlQuery()

                qry.prepare("DELETE FROM Voter WHERE Username= '"+username+"' ")
                

                if(qry.exec()):
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Information)
                    msg.setWindowTitle("Delete Voter")
                    msg.setText("Voter Deleted Successfully")
                    msg.exec_()
                    
                    voter_model = QSqlQueryModel()
                    qry= QSqlQuery()
                    qry.prepare("select Username from Voter")
                    qry.exec()
                    voter_model.setQuery(qry)
                    self.voter_combo.setModel(voter_model)
                    
                    db.commit()
                    db.close()



                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.setWindowTitle("Delete Voter")
                    #msg.setText("Action Failed, Voter Already Exists")
                    msg.setText("Action Failed, "+qry.lastError().text())
                    msg.exec_()
                    db.close()
                    
            elif answer == QMessageBox.No:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setWindowTitle("Delete Voter")
                msg.setText("Voter Not Deleted")
                #msg.setText("Action Failed, "+qry.lastError().text())
                msg.exec_()
        
    def setupUi(self, delete_voter):
       
        delete_voter.setObjectName("delete_voter")
        delete_voter.resize(400, 240)
        delete_voter.setStyleSheet("background-image: url(:/Images/Dialog.png);")

        self.voter_combo = QtWidgets.QComboBox(delete_voter)
        self.voter_combo.setGeometry(QtCore.QRect(120, 100, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(10)
        self.voter_combo.setFont(font)
        self.voter_combo.setStyleSheet("background-color: rgb(53, 84, 118);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.voter_combo.setObjectName("voter_combo")
        
        self.label = QtWidgets.QLabel(delete_voter)
        self.label.setGeometry(QtCore.QRect(80, 40, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.label.setObjectName("label")

        self.delete_2 = QtWidgets.QPushButton(delete_voter)
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
        
        self.cancel = QtWidgets.QPushButton(delete_voter)
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

        self.retranslateUi(delete_voter)
        QtCore.QMetaObject.connectSlotsByName(delete_voter)
        delete_voter.setTabOrder(self.voter_combo, self.delete_2)
        delete_voter.setTabOrder(self.delete_2, self.cancel)

        #####Load Data to Combo Box
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
        

        ####Buttons
        self.cancel.clicked.connect(delete_voter.close)
        self.delete_2.clicked.connect(self.delete_voter)

        
    def retranslateUi(self, delete_voter):
        _translate = QtCore.QCoreApplication.translate
        delete_voter.setWindowTitle(_translate("delete_voter", "Delete Voter"))
        self.delete_2.setText(_translate("delete_voter", "Delete Voter"))
        self.label.setText(_translate("delete_voter", "<html><head/><body><p align=\"center\">select voter to delete</p></body></html>"))
        self.cancel.setText(_translate("delete_voter", "Cancel"))


    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    delete_voter = QtWidgets.QDialog()
    ui = Ui_delete_voter()
    ui.setupUi(delete_voter)
    delete_voter.show()
    sys.exit(app.exec_())
