# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_panel.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

from add_voter import Ui_add_voter
from edit_voter import Ui_edit_voter
from delete_voter import Ui_delete_voter
from add_candidate import Ui_add_candidate
from edit_candidate import Ui_edit_candidate
from delete_candidate import Ui_delete_candidate

import sqlite3

import images

class Ui_admin_panel(object):

    def update_table(self):
        
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database.db")
        db.open()
        
        new_candidate_model = QSqlQueryModel()
        new_candidate_model.setQuery("select * from Candidate where Position = '"+self.position_combo.currentText()+"' order by Votes desc " , db )
        
        self.candidate_table.setModel(new_candidate_model)
        
        db.close()

    def reset_vote(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setWindowTitle("Reset All Votes")
        msg.setText("Are You Sure You Want to Reset All Votes?")
        msg.setStandardButtons(QMessageBox.Yes| QMessageBox.No  )
        msg.setDefaultButton(QMessageBox.No)
        answer = msg.exec_()

        if answer == QMessageBox.Yes:
   
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName("database.db")
            db.open()

            qry = QSqlQuery()
            qry.prepare("UPDATE Candidate set Votes = 0")
                
            if(qry.exec()):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setWindowTitle("Reset All Votes")
                msg.setText("All Votes Have Been Reset Successfully")
                msg.exec_()
                
                db.commit()
                db.close()        
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("Reset All Votes")
                #msg.setText("Action Failed, Voter Already Exists")
                msg.setText("Action Failed, "+qry.lastError().text())
                msg.exec_()
                    
                db.close()

    def open_delete_candidate(self):
        self.delete_candidate = QtWidgets.QDialog()
        self.ui = Ui_delete_candidate()
        self.ui.setupUi(self.delete_candidate)
        self.delete_candidate.exec()

    def open_edit_candidate(self):
        self.edit_candidate = QtWidgets.QDialog()
        self.ui = Ui_edit_candidate()
        self.ui.setupUi(self.edit_candidate)
        self.edit_candidate.exec()
    
    def open_add_candidate(self):
        self.add_candidate = QtWidgets.QDialog()
        self.ui = Ui_add_candidate()
        self.ui.setupUi(self.add_candidate)
        self.add_candidate.exec()

    def delete_all_candidates(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setWindowTitle("Delete All Candidate")
        msg.setText("Are You Sure You Want to Delete All Candidate?")
        msg.setStandardButtons(QMessageBox.Yes| QMessageBox.No  )
        msg.setDefaultButton(QMessageBox.No)
        answer = msg.exec_()

        if answer == QMessageBox.Yes:
   
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName("database.db")
            db.open()

            qry = QSqlQuery()
            qry.prepare("DELETE FROM Candidate ")
                
            if(qry.exec()):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setWindowTitle("Delete All Candidate")
                msg.setText("All Candidate Deleted Successfully")
                msg.exec_()
                
                db.commit()
                db.close()        
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("Delete All Candidate")
                #msg.setText("Action Failed, Voter Already Exists")
                msg.setText("Action Failed, "+qry.lastError().text())
                msg.exec_()
                    
                db.close()
                    
        elif answer == QMessageBox.No:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle("Delete All Candidate")
            msg.setText("Candidate Not Deleted")
            #msg.setText("Action Failed, "+qry.lastError().text())
            msg.exec_()

    def delete_all_voters(self):
        
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setWindowTitle("Delete All Voter")
        msg.setText("Are You Sure You Want to Delete All Voter?")
        msg.setStandardButtons(QMessageBox.Yes| QMessageBox.No  )
        msg.setDefaultButton(QMessageBox.No)
        answer = msg.exec_()

        if answer == QMessageBox.Yes:
   
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName("database.db")
            db.open()

            qry = QSqlQuery()
            qry.prepare("DELETE FROM Voter ")
                
            if(qry.exec()):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setWindowTitle("Delete All Voter")
                msg.setText("All Voter Deleted Successfully")
                msg.exec_()
                
                db.commit()
                db.close()        
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("Delete All Voter")
                #msg.setText("Action Failed, Voter Already Exists")
                msg.setText("Action Failed, "+qry.lastError().text())
                msg.exec_()
                    
                db.close()
                    
        elif answer == QMessageBox.No:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle("Delete All Voter")
            msg.setText("Voter Not Deleted")
            #msg.setText("Action Failed, "+qry.lastError().text())
            msg.exec_()

    def open_delete_voter(self):
        self.delete_voter = QtWidgets.QDialog()
        self.ui = Ui_delete_voter()
        self.ui.setupUi(self.delete_voter)
        self.delete_voter.exec()
    

    def open_edit_voter(self):
        self.edit_voter = QtWidgets.QDialog()
        self.ui = Ui_edit_voter()
        self.ui.setupUi(self.edit_voter)
        self.edit_voter.exec()

    def open_add_voter(self):
        self.add_voter = QtWidgets.QDialog()
        self.ui = Ui_add_voter()
        self.ui.setupUi(self.add_voter)
        self.add_voter.exec()

    def load_candidates(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database.db")
        db.open()
        
        candidate_model = QSqlQueryModel()
        candidate_model.setQuery("select * from Candidate order by Position, Votes desc " ,db)
        self.candidate_table.setModel(candidate_model)
        
        db.close()

    def load_voters(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database.db")
        db.open()
        
        voter_model = QSqlQueryModel()
        voter_model.setQuery("select * from Voter",db)
        self.voter_table.setModel(voter_model)
        
        db.close()
    
    def setupUi(self, admin_panel):
        
        admin_panel.setObjectName("admin_panel")
        admin_panel.resize(720, 580)
        admin_panel.setStyleSheet("background-image: url(:/Images/Admin Panel.png);")

        self.add_candidate = QtWidgets.QPushButton(admin_panel)
        self.add_candidate.setGeometry(QtCore.QRect(60, 410, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.add_candidate.setFont(font)
        self.add_candidate.setStyleSheet("background-image: url(:/Images/Button.png);\n"
"border-color: rgb(55, 113, 164);\n"
"color: rgb(255, 255, 255);")
        self.add_candidate.setAutoDefault(True)
        self.add_candidate.setDefault(False)
        self.add_candidate.setFlat(True)
        self.add_candidate.setObjectName("add_candidate")
        
        self.delete_candidate = QtWidgets.QPushButton(admin_panel)
        self.delete_candidate.setGeometry(QtCore.QRect(60, 460, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.delete_candidate.setFont(font)
        self.delete_candidate.setStyleSheet("background-image: url(:/Images/Button.png);\n"
"border-color: rgb(55, 113, 164);\n"
"color: rgb(255, 255, 255);")
        self.delete_candidate.setAutoDefault(True)
        self.delete_candidate.setDefault(False)
        self.delete_candidate.setFlat(True)
        self.delete_candidate.setObjectName("delete_candidate")

        self.edit_candidate = QtWidgets.QPushButton(admin_panel)
        self.edit_candidate.setGeometry(QtCore.QRect(200, 410, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.edit_candidate.setFont(font)
        self.edit_candidate.setStyleSheet("background-image: url(:/Images/Button.png);\n"
"border-color: rgb(55, 113, 164);\n"
"color: rgb(255, 255, 255);")
        self.edit_candidate.setAutoDefault(True)
        self.edit_candidate.setDefault(False)
        self.edit_candidate.setFlat(True)
        self.edit_candidate.setObjectName("edit_candidate")
        
        self.delete_all_candidate = QtWidgets.QPushButton(admin_panel)
        self.delete_all_candidate.setGeometry(QtCore.QRect(200, 460, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.delete_all_candidate.setFont(font)
        self.delete_all_candidate.setStyleSheet("background-image: url(:/Images/Button.png);\n"
"border-color: rgb(55, 113, 164);\n"
"color: rgb(255, 255, 255);")
        self.delete_all_candidate.setAutoDefault(True)
        self.delete_all_candidate.setDefault(False)
        self.delete_all_candidate.setFlat(True)
        self.delete_all_candidate.setObjectName("delete_all_candidate")
        
        self.reset_votes = QtWidgets.QPushButton(admin_panel)
        self.reset_votes.setGeometry(QtCore.QRect(130, 510, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.reset_votes.setFont(font)
        self.reset_votes.setStyleSheet("background-image: url(:/Images/Button.png);\n"
"border-color: rgb(55, 113, 164);\n"
"color: rgb(255, 255, 255);")
        self.reset_votes.setAutoDefault(True)
        self.reset_votes.setDefault(False)
        self.reset_votes.setFlat(True)
        self.reset_votes.setObjectName("reset_votes")
        
        self.label = QtWidgets.QLabel(admin_panel)
        self.label.setGeometry(QtCore.QRect(130, 130, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.label.setObjectName("label")
        
        self.candidate_table = QtWidgets.QTableView(admin_panel)
        self.candidate_table.setGeometry(QtCore.QRect(20, 180, 351, 211))
        self.candidate_table.setStyleSheet("background:0;\n")
        self.candidate_table.setObjectName("candidate_table")
        
        self.load_candidate = QtWidgets.QPushButton(admin_panel)
        self.load_candidate.setGeometry(QtCore.QRect(330, 130, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.load_candidate.setFont(font)
        self.load_candidate.setStyleSheet("background-image: url(:/Images/Button.png);\n"
"border-color: rgb(55, 113, 164);\n"
"color: rgb(255, 255, 255);")
        self.load_candidate.setAutoDefault(True)
        self.load_candidate.setDefault(False)
        self.load_candidate.setFlat(True)
        self.load_candidate.setObjectName("load_candidate")
        
        self.label_2 = QtWidgets.QLabel(admin_panel)
        self.label_2.setGeometry(QtCore.QRect(508, 130, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.label_2.setObjectName("label_2")
        
        self.add_voter = QtWidgets.QPushButton(admin_panel)
        self.add_voter.setGeometry(QtCore.QRect(430, 410, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.add_voter.setFont(font)
        self.add_voter.setStyleSheet("background-image: url(:/Images/Button.png);\n"
"border-color: rgb(55, 113, 164);\n"
"color: rgb(255, 255, 255);")
        self.add_voter.setAutoDefault(True)
        self.add_voter.setDefault(False)
        self.add_voter.setFlat(True)
        self.add_voter.setObjectName("add_voter")
        
        self.delete_voter = QtWidgets.QPushButton(admin_panel)
        self.delete_voter.setGeometry(QtCore.QRect(430, 460, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.delete_voter.setFont(font)
        self.delete_voter.setStyleSheet("background-image: url(:/Images/Button.png);\n"
"border-color: rgb(55, 113, 164);\n"
"color: rgb(255, 255, 255);")
        self.delete_voter.setAutoDefault(True)
        self.delete_voter.setDefault(False)
        self.delete_voter.setFlat(True)
        self.delete_voter.setObjectName("delete_voter")
        
        self.delete_all_voter = QtWidgets.QPushButton(admin_panel)
        self.delete_all_voter.setGeometry(QtCore.QRect(570, 460, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.delete_all_voter.setFont(font)
        self.delete_all_voter.setStyleSheet("background-image: url(:/Images/Button.png);\n"
"border-color: rgb(55, 113, 164);\n"
"color: rgb(255, 255, 255);")
        self.delete_all_voter.setAutoDefault(True)
        self.delete_all_voter.setDefault(False)
        self.delete_all_voter.setFlat(True)
        self.delete_all_voter.setObjectName("delete_all_voter")
        
        self.edit_voter = QtWidgets.QPushButton(admin_panel)
        self.edit_voter.setGeometry(QtCore.QRect(570, 410, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.edit_voter.setFont(font)
        self.edit_voter.setStyleSheet("background-image: url(:/Images/Button.png);\n"
"border-color: rgb(55, 113, 164);\n"
"color: rgb(255, 255, 255);")
        self.edit_voter.setAutoDefault(True)
        self.edit_voter.setDefault(False)
        self.edit_voter.setFlat(True)
        self.edit_voter.setObjectName("edit_voter")
        
        self.voter_table = QtWidgets.QTableView(admin_panel)
        self.voter_table.setGeometry(QtCore.QRect(460, 180, 220, 211))
        self.voter_table.setStyleSheet("background:0;\n")
        self.voter_table.setObjectName("voter_table")
        
        self.load_voter = QtWidgets.QPushButton(admin_panel)
        self.load_voter.setGeometry(QtCore.QRect(660, 130, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.load_voter.setFont(font)
        self.load_voter.setStyleSheet("background-image: url(:/Images/Button.png);\n"
"border-color: rgb(55, 113, 164);\n"
"color: rgb(255, 255, 255);")
        self.load_voter.setAutoDefault(True)
        self.load_voter.setDefault(False)
        self.load_voter.setFlat(True)
        self.load_voter.setObjectName("load_voter")
        
        self.close = QtWidgets.QPushButton(admin_panel)
        self.close.setGeometry(QtCore.QRect(620, 550, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.close.setFont(font)
        self.close.setStyleSheet("background-image: url(:/Images/Button.png);\n"
"border-color: rgb(55, 113, 164);\n"
"color: rgb(255, 255, 255);")
        self.close.setAutoDefault(True)
        self.close.setDefault(False)
        self.close.setFlat(True)
        self.close.setObjectName("close")

        self.position_combo = QtWidgets.QComboBox(admin_panel)
        self.position_combo.setGeometry(QtCore.QRect(20, 130, 101, 31))
        self.position_combo.setObjectName("vice_combo")
        self.position_combo.setStyleSheet("background-color: rgb(53, 84, 118);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")

        self.retranslateUi(admin_panel)
        QtCore.QMetaObject.connectSlotsByName(admin_panel)

        ###Load Data to Position Combo Box
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database.db")
        db.open()
        
        position_model = QSqlQueryModel()
        qry= QSqlQuery()
        qry.prepare("select * from Position ")
        qry.exec()
        position_model.setQuery(qry)
        self.position_combo.setModel(position_model)

        db.close()
    
        ###Load Voter Table after Opening
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database.db")
        db.open()
        
        voter_model = QSqlQueryModel()
        voter_model.setQuery("select * from Voter",db)
        self.voter_table.setModel(voter_model)
        
        db.close()

        ###Load Candidate Table After Opening
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database.db")
        db.open()
        
        candidate_model = QSqlQueryModel()
        candidate_model.setQuery("select * from Candidate order by Position, Votes desc " ,db)
        self.candidate_table.setModel(candidate_model)
        
        db.close()


        ###Button Functions

        self.load_voter.clicked.connect(self.load_voters)
        self.load_candidate.clicked.connect(self.load_candidates)
        self.position_combo.currentIndexChanged.connect(self.update_table)
        
        self.add_voter.clicked.connect(self.open_add_voter)
        self.add_voter.clicked.connect(self.load_voters)
        
        self.edit_voter.clicked.connect(self.open_edit_voter)
        self.edit_voter.clicked.connect(self.load_voters)

        self.delete_voter.clicked.connect(self.open_delete_voter)
        self.delete_voter.clicked.connect(self.load_voters)
        
        self.delete_all_voter.clicked.connect(self.delete_all_voters)
        self.delete_all_voter.clicked.connect(self.load_voters)
        
        self.add_candidate.clicked.connect(self.open_add_candidate)
        self.add_candidate.clicked.connect(self.load_candidates)
        
        self.edit_candidate.clicked.connect(self.open_edit_candidate)
        self.edit_candidate.clicked.connect(self.load_candidates)
        
        self.delete_candidate.clicked.connect(self.open_delete_candidate)
        self.delete_candidate.clicked.connect(self.load_candidates)
        
        self.delete_all_candidate.clicked.connect(self.delete_all_candidates)
        self.delete_all_candidate.clicked.connect(self.load_candidates)
        
        self.reset_votes.clicked.connect(self.reset_vote)
        self.reset_votes.clicked.connect(self.load_candidates)
        
        self.close.clicked.connect(admin_panel.close)
        

        
    def retranslateUi(self, admin_panel):
        _translate = QtCore.QCoreApplication.translate
        admin_panel.setWindowTitle(_translate("admin_panel", "Administrator Panel"))
        self.add_candidate.setText(_translate("admin_panel", "Add Candidate"))
        self.delete_candidate.setText(_translate("admin_panel", "Delete Candidate"))
        self.edit_candidate.setText(_translate("admin_panel", "Edit Candidate"))
        self.delete_all_candidate.setText(_translate("admin_panel", "Delete All Candidate"))
        self.reset_votes.setText(_translate("admin_panel", "Reset Votes"))
        self.label.setText(_translate("admin_panel", "<html><head/><body><p align=\"center\">Candidates</p></body></html>"))
        self.load_candidate.setText(_translate("admin_panel", "All"))
        self.label_2.setText(_translate("admin_panel", "<html><head/><body><p align=\"center\">Voters</p></body></html>"))
        self.add_voter.setText(_translate("admin_panel", "Add Voter"))
        self.delete_voter.setText(_translate("admin_panel", "Delete Voter"))
        self.delete_all_voter.setText(_translate("admin_panel", "Delete All Voter"))
        self.edit_voter.setText(_translate("admin_panel", "Edit Voter"))
        self.load_voter.setText(_translate("admin_panel", "Load"))
        self.close.setText(_translate("admin_panel", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_panel = QtWidgets.QDialog()
    ui = Ui_admin_panel()
    ui.setupUi(admin_panel)
    admin_panel.show()
    sys.exit(app.exec_())
