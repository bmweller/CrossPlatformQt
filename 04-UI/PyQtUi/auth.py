from PyQt5.QtSql import *
import helper


class Auth(object):
    def __init__(self):
        self


    def do_login(self, username, password):
        query = QSqlQuery()
        query.prepare("select id from qtapp_users where username = :username and password = :password")
        query.bindValue(":username", username)
        query.bindValue(":password", helper.compute_hash(password))
        query.exec_()
        if query.next():
            return True
        return False
