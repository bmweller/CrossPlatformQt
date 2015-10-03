import sip
import sys

from PyQt5.QtWidgets import QApplication
from logindialog import LoginDialog
from mainwindow import MainWindow
import helper

sip.setapi("QString", 2)

if __name__ == "__main__":
    a = QApplication(sys.argv)
    helper.db_connect()

    loginDialog = LoginDialog()

    result = -1
    authenticated = False
    failed = 0
    while not authenticated and failed < 3:
        result = loginDialog.exec_()
        if result == LoginDialog.Success:  # or result == LoginDialog.Rejected:
            authenticated = True
        elif result == LoginDialog.Failed:  # or result == LoginDialog.Rejected:
            failed += 1
        elif result == LoginDialog.Exit:
            break

    if authenticated:
        w = MainWindow()
        w.show()
        a.exec_()

    sys.exit(-1)
