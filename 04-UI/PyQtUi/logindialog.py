from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication
from PyQt5.QtCore import Qt

from ui_logindialog import Ui_LoginDialog
from auth import Auth


# try:
#     _fromUtf8 = QtCore.QString.fromUtf8
# except AttributeError:
#     def _fromUtf8(s):
#         return s

try:
    _encoding = QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)


class LoginDialog(QDialog, Ui_LoginDialog):
    Exit, Success, Failed, Rejected = range(0, 4)

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.on_accept)
        self.accepted.connect(self.on_accept)
        self.buttonBox.rejected.connect(self.on_cancel)

    def closeEvent(self, event):
        self.setResult(self.Exit)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.setResult(self.Rejected)

    def on_cancel(self):
        self.setResult(self.Exit)

    def on_accept(self):

        auth = Auth()
        if auth.do_login(self.txtUsername.text(), self.txtPassword.text()):
            self.setResult(self.Success)
        else:
            msg_box = QMessageBox(self)
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle(_translate("LoginDialog", "Pythonthusiast", None))
            msg_box.setText(_translate("LoginDialog", "Either incorrect username and/or password. Try again!", None))
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
            self.setResult(self.Failed)

    def on_reject(self):
        self.setResult(self.Rejected)
