from PyQt5.QtCore import *
from PyQt5.QtSql import *


def db_connect():
    db = QSqlDatabase.addDatabase("QSQLITE")
    filename = "pythonthusiast.db"
    database = QFile(filename)
    if not database.exists():
        qDebug("Database not found. Creating and opening")
        db.setDatabaseName(filename)
        db.open()
        query = QSqlQuery()
        query.exec_("create table qtapp_users "
                    "(id integer primary key autoincrement, "
                    "username varchar(30), "
                    "password varchar(255))")
        query.prepare("insert into qtapp_users(username, password) values(:username, :password)")
        query.bindValue(":username", "eko")
        query.bindValue(":password", compute_hash("password"))
        query.exec_()
    else:
        qDebug("Database found. Opening")
        db.setDatabaseName(filename)
        db.open()
    return db.isOpen()


def compute_hash(original):
    # a much more Qt centric
    return QCryptographicHash.hash(original.encode(encoding='UTF-8'), QCryptographicHash.Md5).toHex()
    # return QCryptographicHash.hash(original, QCryptographicHash.Md5).toHex()
