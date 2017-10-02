# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(630, 382)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Piboto Condensed"))
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.ref = QtGui.QPushButton(Form)
        self.ref.setGeometry(QtCore.QRect(10, 340, 101, 31))
        self.ref.setObjectName(_fromUtf8("ref"))
        self.ala = QtGui.QPushButton(Form)
        self.ala.setGeometry(QtCore.QRect(120, 340, 101, 31))
        self.ala.setObjectName(_fromUtf8("ala"))
        self.qui = QtGui.QPushButton(Form)
        self.qui.setGeometry(QtCore.QRect(520, 340, 101, 31))
        self.qui.setObjectName(_fromUtf8("qui"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 611, 281))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.time_l = QtGui.QLabel(self.layoutWidget)
        self.time_l.setObjectName(_fromUtf8("time_l"))
        self.verticalLayout.addWidget(self.time_l)
        self.hum_l = QtGui.QLabel(self.layoutWidget)
        self.hum_l.setObjectName(_fromUtf8("hum_l"))
        self.verticalLayout.addWidget(self.hum_l)
        self.temp_l = QtGui.QLabel(self.layoutWidget)
        self.temp_l.setObjectName(_fromUtf8("temp_l"))
        self.verticalLayout.addWidget(self.temp_l)
        self.t_ala = QtGui.QLabel(self.layoutWidget)
        self.t_ala.setObjectName(_fromUtf8("t_ala"))
        self.verticalLayout.addWidget(self.t_ala)
        self.h_ala = QtGui.QLabel(self.layoutWidget)
        self.h_ala.setObjectName(_fromUtf8("h_ala"))
        self.verticalLayout.addWidget(self.h_ala)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.temp_v = QtGui.QLabel(self.layoutWidget)
        self.temp_v.setObjectName(_fromUtf8("temp_v"))
        self.verticalLayout_2.addWidget(self.temp_v)
        self.hum_v = QtGui.QLabel(self.layoutWidget)
        self.hum_v.setObjectName(_fromUtf8("hum_v"))
        self.verticalLayout_2.addWidget(self.hum_v)
        self.tim_v = QtGui.QLabel(self.layoutWidget)
        self.tim_v.setObjectName(_fromUtf8("tim_v"))
        self.verticalLayout_2.addWidget(self.tim_v)
        self.t_ala_v = QtGui.QLabel(self.layoutWidget)
        self.t_ala_v.setObjectName(_fromUtf8("t_ala_v"))
        self.verticalLayout_2.addWidget(self.t_ala_v)
        self.h_ala_v = QtGui.QLabel(self.layoutWidget)
        self.h_ala_v.setObjectName(_fromUtf8("h_ala_v"))
        self.verticalLayout_2.addWidget(self.h_ala_v)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.ala_enter = QtGui.QLineEdit(Form)
        self.ala_enter.setGeometry(QtCore.QRect(230, 340, 61, 33))
        self.ala_enter.setObjectName(_fromUtf8("ala_enter"))
        self.ala_2 = QtGui.QPushButton(Form)
        self.ala_2.setGeometry(QtCore.QRect(300, 340, 101, 31))
        self.ala_2.setObjectName(_fromUtf8("ala_2"))
        self.ala_enter_2 = QtGui.QLineEdit(Form)
        self.ala_enter_2.setGeometry(QtCore.QRect(410, 340, 61, 33))
        self.ala_enter_2.setObjectName(_fromUtf8("ala_enter_2"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.ala, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ala_enter.copy)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.ref.setText(_translate("Form", "Refresh", None))
        self.ala.setText(_translate("Form", "Set T Alarm", None))
        self.qui.setText(_translate("Form", "Quit", None))
        self.time_l.setText(_translate("Form", "Temp :", None))
        self.hum_l.setText(_translate("Form", "Hum :", None))
        self.temp_l.setText(_translate("Form", "Time :", None))
        self.t_ala.setText(_translate("Form", "Temp Alarm :", None))
        self.h_ala.setText(_translate("Form", "Hum Alarm :", None))
        self.temp_v.setText(_translate("Form", "0.00", None))
        self.hum_v.setText(_translate("Form", "0.00", None))
        self.tim_v.setText(_translate("Form", "0.00", None))
        self.t_ala_v.setText(_translate("Form", "0.00", None))
        self.h_ala_v.setText(_translate("Form", "0.00", None))
        self.ala_2.setText(_translate("Form", "Set H Alarm", None))

