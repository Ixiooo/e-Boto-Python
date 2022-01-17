# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'voter_panel.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

import images

class Ui_voter_panel(object):

    def load_candidate(self):
        ###Data to Each Combo Box
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database.db")
        db.open()
        
        president_model = QSqlQueryModel()
        qry = QSqlQuery()
        qry.prepare("select Name from Candidate where Position = 'President' ")
        qry.exec()
        president_model.setQuery(qry)
        self.president_combo.setModel(president_model)

        vice_model = QSqlQueryModel()
        qry= QSqlQuery()
        qry.prepare("select Name from Candidate where Position = 'Vice President' ")
        qry.exec()
        vice_model.setQuery(qry)
        self.vice_combo.setModel(vice_model)

        secretary_model = QSqlQueryModel()
        qry= QSqlQuery()
        qry.prepare("select Name from Candidate where Position = 'Secretary' ")
        qry.exec()
        secretary_model.setQuery(qry)
        self.secretary_combo.setModel(secretary_model)

        treasurer_model = QSqlQueryModel()
        qry= QSqlQuery()
        qry.prepare("select Name from Candidate where Position = 'Treasurer' ")
        qry.exec()
        treasurer_model.setQuery(qry)
        self.treasurer_combo.setModel(treasurer_model)

        auditor_model = QSqlQueryModel()
        qry= QSqlQuery()
        qry.prepare("select Name from Candidate where Position = 'Auditor' ")
        qry.exec()
        auditor_model.setQuery(qry)
        self.auditor_combo.setModel(auditor_model)

        pio_model = QSqlQueryModel()
        qry= QSqlQuery()
        qry.prepare("select Name from Candidate where Position = 'PIO' ")
        qry.exec()
        pio_model.setQuery(qry)
        self.pio_combo.setModel(pio_model)

        sergeant_model = QSqlQueryModel()
        qry= QSqlQuery()
        qry.prepare("select Name from Candidate where Position = 'Sergant at Arms' ")
        qry.exec()
        sergeant_model.setQuery(qry)
        self.sergeant_combo.setModel(sergeant_model)
              
        db.close()
    
    def display_voted(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def change_voted(self):
        self.stackedWidget.setCurrentIndex(0)

    def pass_voted(self):
        
        ###Pass voted candidates to next page
        self.voted_president.setText(self.president_combo.currentText())
        self.voted_vice.setText(self.vice_combo.currentText())
        self.vote_secretary.setText(self.secretary_combo.currentText())
        self.voted_treasurer.setText(self.treasurer_combo.currentText())
        self.voted_auditor.setText(self.auditor_combo.currentText())
        self.voted_pio.setText(self.pio_combo.currentText())
        self.voted_sergeant.setText(self.sergeant_combo.currentText())

    def submit_votes(self):

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database.db")
        db.open()

        qry = QSqlQuery()
        qry.prepare("Update Candidate set Votes = Votes + 1 where Name IN ('"+self.president_combo.currentText()+"', '"+self.vice_combo.currentText()+"', '"+self.secretary_combo.currentText()+"', '"+self.treasurer_combo.currentText()+"', '"+self.auditor_combo.currentText()+"', '"+self.pio_combo.currentText()+"', '"+self.sergeant_combo.currentText()+"')") 

        if (qry.exec()):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle("Submit Votes")
            msg.setText("Votes Submitted Successfully")
            msg.exec_()
            db.close()
            

            
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Submit Votes")
            msg.setText("Error in Submitting Votes")
            msg.exec_()

        
        db.close()
        
    def setupUi(self, voter_panel):

        
        voter_panel.setObjectName("voter_panel")
        voter_panel.resize(720, 600)
        voter_panel.setStyleSheet("background-image: url(:/Images/Voter Panel.PNG);")

        self.stackedWidget = QtWidgets.QStackedWidget(voter_panel)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 721, 601))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Book")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        
        self.presLabel = QtWidgets.QLabel(self.page)
        self.presLabel.setGeometry(QtCore.QRect(120, 230, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(22)
        self.presLabel.setFont(font)
        self.presLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.presLabel.setObjectName("presLabel")
        
        self.president_combo = QtWidgets.QComboBox(self.page)
        self.president_combo.setGeometry(QtCore.QRect(110, 270, 151, 31))
        self.president_combo.setObjectName("president_combo")
        self.president_combo.setStyleSheet("background-color: rgb(53, 84, 118);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        
        self.vpLabel = QtWidgets.QLabel(self.page)
        self.vpLabel.setGeometry(QtCore.QRect(300, 230, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(22)
        self.vpLabel.setFont(font)
        self.vpLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.vpLabel.setObjectName("vpLabel")

        
        self.vice_combo = QtWidgets.QComboBox(self.page)
        self.vice_combo.setGeometry(QtCore.QRect(290, 270, 151, 31))
        self.vice_combo.setObjectName("vice_combo")
        self.vice_combo.setStyleSheet("background-color: rgb(53, 84, 118);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        
        self.secLabel = QtWidgets.QLabel(self.page)
        self.secLabel.setGeometry(QtCore.QRect(480, 230, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(22)
        self.secLabel.setFont(font)
        self.secLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.secLabel.setObjectName("secLabel")

        
        self.secretary_combo = QtWidgets.QComboBox(self.page)
        self.secretary_combo.setGeometry(QtCore.QRect(470, 270, 151, 31))
        self.secretary_combo.setObjectName("secretary_combo")
        self.secretary_combo.setStyleSheet("background-color: rgb(53, 84, 118);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        
        self.treasurer_combo = QtWidgets.QComboBox(self.page)
        self.treasurer_combo.setGeometry(QtCore.QRect(20, 420, 151, 31))
        self.treasurer_combo.setObjectName("treasurer_combo")
        self.treasurer_combo.setStyleSheet("background-color: rgb(53, 84, 118);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        
        self.tresLabel = QtWidgets.QLabel(self.page)
        self.tresLabel.setGeometry(QtCore.QRect(30, 380, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(22)
        self.tresLabel.setFont(font)
        self.tresLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.tresLabel.setObjectName("tresLabel")

        
        self.audLabel = QtWidgets.QLabel(self.page)
        self.audLabel.setGeometry(QtCore.QRect(190, 380, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(22)
        self.audLabel.setFont(font)
        self.audLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.audLabel.setObjectName("audLabel")

        
        self.auditor_combo = QtWidgets.QComboBox(self.page)
        self.auditor_combo.setGeometry(QtCore.QRect(190, 420, 151, 31))
        self.auditor_combo.setObjectName("auditor_combo")
        self.auditor_combo.setStyleSheet("background-color: rgb(53, 84, 118);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        
        self.pio_combo = QtWidgets.QComboBox(self.page)
        self.pio_combo.setGeometry(QtCore.QRect(380, 420, 151, 31))
        self.pio_combo.setObjectName("pio_combo")
        self.pio_combo.setStyleSheet("background-color: rgb(53, 84, 118);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        
        self.pioLabel = QtWidgets.QLabel(self.page)
        self.pioLabel.setGeometry(QtCore.QRect(370, 380, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(22)
        self.pioLabel.setFont(font)
        self.pioLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.pioLabel.setObjectName("pioLabel")

        
        self.sergeant_combo = QtWidgets.QComboBox(self.page)
        self.sergeant_combo.setGeometry(QtCore.QRect(550, 420, 151, 31))
        self.sergeant_combo.setObjectName("sergeant_combo")
        self.sergeant_combo.setStyleSheet("background-color: rgb(53, 84, 118);\n"
"selection-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        
        self.sergeantLabel = QtWidgets.QLabel(self.page)
        self.sergeantLabel.setGeometry(QtCore.QRect(540, 380, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(22)
        self.sergeantLabel.setFont(font)
        self.sergeantLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.sergeantLabel.setObjectName("sergeantLabel")

        
        self.vote = QtWidgets.QPushButton(self.page)
        self.vote.setGeometry(QtCore.QRect(300, 520, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.vote.setFont(font)
        self.vote.setStyleSheet("background-image: url(C:/Users/Ixio/Documents/PythonFinal/Images/Button.png);\n"
"border-color: rgb(55, 113, 164);\n"
"color: rgb(255, 255, 255);")
        self.vote.setFlat(True)
        self.vote.setObjectName("vote")

        
        self.presLabel_4 = QtWidgets.QLabel(self.page)
        self.presLabel_4.setGeometry(QtCore.QRect(0, 90, 721, 101))
        font = QtGui.QFont()
        font.setFamily("Liberator Light")
        font.setPointSize(22)
        self.presLabel_4.setFont(font)
        self.presLabel_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.presLabel_4.setObjectName("presLabel_4")

        
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(570, 170, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-image: url(:/Images/Button.png);\n"
"border-color: rgb(55, 113, 164);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")

        
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.tresLabel_2 = QtWidgets.QLabel(self.page_2)
        self.tresLabel_2.setGeometry(QtCore.QRect(200, 360, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(22)
        self.tresLabel_2.setFont(font)
        self.tresLabel_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.tresLabel_2.setObjectName("tresLabel_2")
        self.presLabel_2 = QtWidgets.QLabel(self.page_2)
        self.presLabel_2.setGeometry(QtCore.QRect(210, 210, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(22)
        self.presLabel_2.setFont(font)
        self.presLabel_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.presLabel_2.setObjectName("presLabel_2")

        
        self.vpLabel_2 = QtWidgets.QLabel(self.page_2)
        self.vpLabel_2.setGeometry(QtCore.QRect(200, 260, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(22)
        self.vpLabel_2.setFont(font)
        self.vpLabel_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.vpLabel_2.setObjectName("vpLabel_2")

        
        self.sergeantLabel_2 = QtWidgets.QLabel(self.page_2)
        self.sergeantLabel_2.setGeometry(QtCore.QRect(190, 510, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(22)
        self.sergeantLabel_2.setFont(font)
        self.sergeantLabel_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.sergeantLabel_2.setObjectName("sergeantLabel_2")

        
        self.audLabel_2 = QtWidgets.QLabel(self.page_2)
        self.audLabel_2.setGeometry(QtCore.QRect(190, 410, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(22)
        self.audLabel_2.setFont(font)
        self.audLabel_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.audLabel_2.setObjectName("audLabel_2")

        
        self.secLabel_2 = QtWidgets.QLabel(self.page_2)
        self.secLabel_2.setGeometry(QtCore.QRect(200, 310, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(22)
        self.secLabel_2.setFont(font)
        self.secLabel_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.secLabel_2.setObjectName("secLabel_2")

        
        self.pioLabel_2 = QtWidgets.QLabel(self.page_2)
        self.pioLabel_2.setGeometry(QtCore.QRect(190, 460, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Bold")
        font.setPointSize(22)
        self.pioLabel_2.setFont(font)
        self.pioLabel_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.pioLabel_2.setObjectName("pioLabel_2")

        
        self.voted_president = QtWidgets.QLabel(self.page_2)
        self.voted_president.setGeometry(QtCore.QRect(370, 210, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.voted_president.setFont(font)
        self.voted_president.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.voted_president.setObjectName("voted_president")

        
        self.voted_vice = QtWidgets.QLabel(self.page_2)
        self.voted_vice.setGeometry(QtCore.QRect(370, 260, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.voted_vice.setFont(font)
        self.voted_vice.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.voted_vice.setObjectName("voted_vice")

        
        self.vote_secretary = QtWidgets.QLabel(self.page_2)
        self.vote_secretary.setGeometry(QtCore.QRect(370, 310, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.vote_secretary.setFont(font)
        self.vote_secretary.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.vote_secretary.setObjectName("vote_secretary")

        
        self.voted_treasurer = QtWidgets.QLabel(self.page_2)
        self.voted_treasurer.setGeometry(QtCore.QRect(370, 360, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.voted_treasurer.setFont(font)
        self.voted_treasurer.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.voted_treasurer.setObjectName("voted_treasurer")

        
        self.voted_auditor = QtWidgets.QLabel(self.page_2)
        self.voted_auditor.setGeometry(QtCore.QRect(370, 410, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.voted_auditor.setFont(font)
        self.voted_auditor.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.voted_auditor.setObjectName("voted_auditor")

        
        self.voted_pio = QtWidgets.QLabel(self.page_2)
        self.voted_pio.setGeometry(QtCore.QRect(370, 460, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.voted_pio.setFont(font)
        self.voted_pio.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.voted_pio.setObjectName("voted_pio")

        
        self.voted_sergeant = QtWidgets.QLabel(self.page_2)
        self.voted_sergeant.setGeometry(QtCore.QRect(370, 510, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.voted_sergeant.setFont(font)
        self.voted_sergeant.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.voted_sergeant.setObjectName("voted_sergeant")

        
        self.vote_final = QtWidgets.QPushButton(self.page_2)
        self.vote_final.setGeometry(QtCore.QRect(570, 540, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.vote_final.setFont(font)
        self.vote_final.setStyleSheet("background-image: url(:/Images/Button.png);\n"
"border-color: rgb(55, 113, 164);\n"
"color: rgb(255, 255, 255);")
        self.vote_final.setFlat(True)
        self.vote_final.setObjectName("vote_final")

        self.back = QtWidgets.QPushButton(self.page_2)
        self.back.setGeometry(QtCore.QRect(30, 540, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.back.setFont(font)
        self.back.setStyleSheet("background-image: url(:/Images/Button.png);\n"
"border-color: rgb(55, 113, 164);\n"
"color: rgb(255, 255, 255);")
        self.back.setFlat(True)
        self.back.setObjectName("vote_final")
        
        self.presLabel_3 = QtWidgets.QLabel(self.page_2)
        self.presLabel_3.setGeometry(QtCore.QRect(10, 110, 711, 101))
        font = QtGui.QFont()
        font.setFamily("Liberator Light")
        font.setPointSize(22)
        self.presLabel_3.setFont(font)
        self.presLabel_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:0;\n"
"")
        self.presLabel_3.setObjectName("presLabel_3")
        self.tresLabel_2.raise_()
        self.presLabel_2.raise_()
        self.vpLabel_2.raise_()
        self.sergeantLabel_2.raise_()
        self.audLabel_2.raise_()
        self.secLabel_2.raise_()
        self.pioLabel_2.raise_()
        self.voted_president.raise_()
        self.voted_vice.raise_()
        self.vote_secretary.raise_()
        self.voted_treasurer.raise_()
        self.voted_auditor.raise_()
        self.voted_pio.raise_()
        self.voted_sergeant.raise_()
        self.presLabel_3.raise_()
        self.vote_final.raise_()
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(voter_panel)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(voter_panel)

        ####Data to Combo Box

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database.db")
        db.open()
        
        president_model = QSqlQueryModel()
        qry = QSqlQuery()
        qry.prepare("select Name from Candidate where Position = 'President' ")
        qry.exec()
        president_model.setQuery(qry)
        self.president_combo.setModel(president_model)

        vice_model = QSqlQueryModel()
        qry= QSqlQuery()
        qry.prepare("select Name from Candidate where Position = 'Vice President' ")
        qry.exec()
        vice_model.setQuery(qry)
        self.vice_combo.setModel(vice_model)

        secretary_model = QSqlQueryModel()
        qry= QSqlQuery()
        qry.prepare("select Name from Candidate where Position = 'Secretary' ")
        qry.exec()
        secretary_model.setQuery(qry)
        self.secretary_combo.setModel(secretary_model)

        treasurer_model = QSqlQueryModel()
        qry= QSqlQuery()
        qry.prepare("select Name from Candidate where Position = 'Treasurer' ")
        qry.exec()
        treasurer_model.setQuery(qry)
        self.treasurer_combo.setModel(treasurer_model)

        auditor_model = QSqlQueryModel()
        qry= QSqlQuery()
        qry.prepare("select Name from Candidate where Position = 'Auditor' ")
        qry.exec()
        auditor_model.setQuery(qry)
        self.auditor_combo.setModel(auditor_model)

        pio_model = QSqlQueryModel()
        qry= QSqlQuery()
        qry.prepare("select Name from Candidate where Position = 'PIO' ")
        qry.exec()
        pio_model.setQuery(qry)
        self.pio_combo.setModel(pio_model)
        
        sergeant_model = QSqlQueryModel()
        qry= QSqlQuery()
        qry.prepare("select Name from Candidate where Position = 'Sergant at Arms' ")
        qry.exec()
        sergeant_model.setQuery(qry)
        self.sergeant_combo.setModel(sergeant_model)
        
        
        db.close()
        

        ####Buttons
        self.vote.clicked.connect(self.display_voted)
        self.vote.clicked.connect(self.pass_voted)
        self.back.clicked.connect(self.change_voted)
        self.pushButton.clicked.connect(self.load_candidate)
        self.vote_final.clicked.connect(self.submit_votes)
        self.vote_final.clicked.connect(voter_panel.close)
        
    def retranslateUi(self, voter_panel):
        _translate = QtCore.QCoreApplication.translate
        voter_panel.setWindowTitle(_translate("voter_panel", "Voter Panel"))
        self.presLabel.setText(_translate("voter_panel", "<html><head/><body><p align=\"center\">President</p></body></html>"))
        self.vpLabel.setText(_translate("voter_panel", "<html><head/><body><p align=\"center\">vice president</p></body></html>"))
        self.secLabel.setText(_translate("voter_panel", "<html><head/><body><p align=\"center\">secretary</p></body></html>"))
        self.tresLabel.setText(_translate("voter_panel", "<html><head/><body><p align=\"center\">TREASURER</p></body></html>"))
        self.audLabel.setText(_translate("voter_panel", "<html><head/><body><p align=\"center\">auditor</p></body></html>"))
        self.pioLabel.setText(_translate("voter_panel", "<html><head/><body><p align=\"center\">pio</p></body></html>"))
        self.sergeantLabel.setText(_translate("voter_panel", "<html><head/><body><p align=\"center\">sergeant at arms</p></body></html>"))
        self.vote.setText(_translate("voter_panel", "Vote"))
        self.presLabel_4.setText(_translate("voter_panel", "<html><head/><body><p align=\"center\">PICK YOUR DESIRED CANDIDATE AND VOTE WISELY</p></body></html>"))
        self.pushButton.setText(_translate("voter_panel", "Load Candidates"))
        self.tresLabel_2.setText(_translate("voter_panel", "<html><head/><body><p align=\"center\">TREASURER</p></body></html>"))
        self.presLabel_2.setText(_translate("voter_panel", "<html><head/><body><p align=\"center\">President</p></body></html>"))
        self.vpLabel_2.setText(_translate("voter_panel", "<html><head/><body><p align=\"center\">vice president</p></body></html>"))
        self.sergeantLabel_2.setText(_translate("voter_panel", "<html><head/><body><p align=\"center\">sergeant at arms</p></body></html>"))
        self.audLabel_2.setText(_translate("voter_panel", "<html><head/><body><p align=\"center\">auditor</p></body></html>"))
        self.secLabel_2.setText(_translate("voter_panel", "<html><head/><body><p align=\"center\">secretary</p></body></html>"))
        self.pioLabel_2.setText(_translate("voter_panel", "<html><head/><body><p align=\"center\">pio</p></body></html>"))
        self.voted_president.setText(_translate("voter_panel", "Chosen Candidate"))
        self.voted_vice.setText(_translate("voter_panel", "Chosen Candidate"))
        self.vote_secretary.setText(_translate("voter_panel", "Chosen Candidate"))
        self.voted_treasurer.setText(_translate("voter_panel", "Chosen Candidate"))
        self.voted_auditor.setText(_translate("voter_panel", "Chosen Candidate"))
        self.voted_pio.setText(_translate("voter_panel", "Chosen Candidate"))
        self.voted_sergeant.setText(_translate("voter_panel", "Chosen Candidate"))
        self.vote_final.setText(_translate("voter_panel", "Vote"))
        self.presLabel_3.setText(_translate("voter_panel", "<html><head/><body><p align=\"center\">Please Verify and Check Your Chosen Candidate </p><p align=\"center\">Before Pressing the Vote Button</p></body></html>"))
        self.back.setText(_translate("voter_panel", "Back"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    voter_panel = QtWidgets.QDialog()
    ui = Ui_voter_panel()
    ui.setupUi(voter_panel)
    voter_panel.show()
    sys.exit(app.exec_())
