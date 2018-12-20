# -*- coding:utf-8 -*-
# Author:      LiuSha
from __future__ import (
    division,
    print_function,
    unicode_literals,
)

import MySQLdb
import logging

class DB(object):

    __host       = None
    __port       = None
    __user       = None
    __password   = None
    __database   = None
    __session    = None
    __connection = None

    def __init__(self, host, port, user, password, database):
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__database = database

    def __conn(self):
        try:
            return MySQLdb.Connect(
                host=self.__host, port=self.__port,
                user=self.__user, passwd=self.__password,
                db=self.__database, charset='utf8',
                use_unicode=True, connect_timeout=3
            )

        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0],e.args[1]))

    def __open(self, dict_cursor=True):
        try:
            conn = self.__conn()
            self.__connection = conn
            if dict_cursor:
                self.__session = conn.cursor(MySQLdb.cursors.DictCursor)
            else:
                self.__session = conn.cursor()

        except (AttributeError, MySQLdb.OperationalError):
            self.__connection and self.__connection.close()

            #Re connection
            conn = self.__conn()
            self.__connection = conn
            if dict_cursor:
                self.__session = conn.cursor(MySQLdb.cursors.DictCursor)
            else:
                self.__session = conn.cursor()

    def __close(self):
        self.__session.close()
        self.__connection.close()

    def select(self, cmd):
        self.__open()
        result = self.__session.execute(cmd)
        number_rows = self.__session.rowcount
        number_columns = self.__session.description

	logging.debug("SQL=" + cmd)

        if number_rows >= 1 and number_columns > 1:
            result = [item for item in self.__session.fetchall()]
        else:
            result = [item.pop() for item in self.__session.fetchall()]

        self.__close()

        return result

    def update(self, cmd):
        self.__open()
        self.__session.execute(cmd)
        self.__connection.commit()

	logging.debug("SQL=" + cmd)

        update_rows = self.__session.rowcount
        self.__close()

        return update_rows

    def insert(self, cmd):
        self.__open()
        self.__session.execute(cmd)
        self.__connection.commit()

	logging.debug("SQL=" + cmd)

        lastrowid = self.__session.lastrowid
        self.__close()

        return lastrowid

    def delete(self, cmd):
        self.__open()
        self.__session.execute(cmd)
        self.__connection.commit()

	logging.debug("SQL=" + cmd)

        delete_rows = self.__session.rowcount
        self.__close()

        return delete_rows

