
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication

from ui_mainwindow import Ui_MainWindow


try:
    _encoding = QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.actionE_xit.triggered.connect(self.on_exit)
        self.action_About.triggered.connect(self.on_about)

    def on_exit(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowTitle(_translate("MainWindow", "Pythonthusiast", None))
        msg_box.setText(_translate("MainWindow", "Are you sure you want to quit?", None))
        msg_box.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        msg_box.setDefaultButton(QMessageBox.Yes)
        if msg_box.exec_() == QMessageBox.Yes:
            q_app = QApplication.instance()
            q_app.quit()

    def on_about(self):
        msg_box = QMessageBox(self)
        msg_box.setIconPixmap(QPixmap(":/images/sherlock.png"))
        msg_box.setWindowTitle(_translate("MainWindow", "Pythonthusiast", None))
        msg_box.setText(_translate("MainWindow", "Well Watson, isn't it obvious to you that Qt rocks?", None))
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()
