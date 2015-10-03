# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logindialog.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(266, 139)
        self.buttonBox = QtWidgets.QDialogButtonBox(LoginDialog)
        self.buttonBox.setGeometry(QtCore.QRect(90, 100, 161, 32))
        self.buttonBox.setFocusPolicy(QtCore.Qt.TabFocus)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(LoginDialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(LoginDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.label_2.setObjectName("label_2")
        self.txtPassword = QtWidgets.QLineEdit(LoginDialog)
        self.txtPassword.setGeometry(QtCore.QRect(80, 60, 161, 23))
        self.txtPassword.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.txtUsername = QtWidgets.QLineEdit(LoginDialog)
        self.txtUsername.setGeometry(QtCore.QRect(80, 20, 161, 23))
        self.txtUsername.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txtUsername.setObjectName("txtUsername")

        self.retranslateUi(LoginDialog)
        self.buttonBox.accepted.connect(LoginDialog.accept)
        self.buttonBox.rejected.connect(LoginDialog.reject)
        self.txtPassword.returnPressed.connect(LoginDialog.accept)
        self.txtUsername.textEdited['QString'].connect(self.txtPassword.clear)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)
        LoginDialog.setTabOrder(self.txtUsername, self.txtPassword)
        LoginDialog.setTabOrder(self.txtPassword, self.buttonBox)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Dialog"))
        self.label.setText(_translate("LoginDialog", "Username"))
        self.label_2.setText(_translate("LoginDialog", "Password"))

