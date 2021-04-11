#!/usr/bin/env python
# coding: utf-8

#기본 import 함수들
import os
import ibm_db_dbi as db  #db2 연결용
import cx_Oracle  #oracle 연결용
from psycopg2 import connect  #Postgre연결용
import pymssql  #sql server(MS SQL) 연결용

oracle_install_space = ""
#oracle_install_space = "C:\oracle\instantclient_19_8"


#각 DB들 연결하는 함수

def db2_con(Database, Host, PORT, Username, Password):
    db_connection = db.connect(
        'DATABASE=' + str(Database) + ';'
        'HOSTNAME=' + str(Host) + ';'
        'PORT=' + str(PORT) + ';'
        'UID = ' + str(Username) + ';'
        'PWD= ' + str(Password) + ';', '', ' ')
    return db_connection


def oracle_con(Database, Host, PORT, Username, Password, oracle_install_space):
    #oracle과 instantcleint있어야만 실행이 가능함
    location = oracle_install_space
    os.environ["PATH"] = location + ';' + os.environ["PATH"]

    oracle_connection = cx_Oracle.connect(
        str(Username) + '/' + str(Password) + '@' + str(Host) + ':' +
        str(PORT) + '/' + str(Database))
    return oracle_connection


def sql_server_con(Database, Host, PORT, Username, Password, charset='utf8'):
    sql_server_connection = pymssql.connect(database=str(Database),
                                            server=str(Host),
                                            port=int(PORT),
                                            user=str(Username),
                                            password=str(Password),
                                            charset=charset)
    return sql_server_connection


def postgre_con(Database, Host, PORT, Username, Password):
    postgre_connection = connect(database=str(Database),
                                 host=str(Host),
                                 port=int(PORT),
                                 user=str(Username),
                                 password=str(Password))
    return postgre_connection


#전체 통합 연결 함수
def python_db_connection(DB_type,
                         Database,
                         Host,
                         PORT,
                         Username,
                         Password,
                         space=oracle_install_space):
    if DB_type == 'oracle':

        connection_result = oracle_con(Database, Host, PORT, Username,
                                       Password, space)
    elif DB_type == 'db2':
        connection_result = db2_con(Database, Host, PORT, Username, Password)
    elif DB_type == 'sql server':
        connection_result = sql_server_con(Database,
                                           Host,
                                           PORT,
                                           Username,
                                           Password,
                                           charset='utf8')
    elif DB_type == 'postgre':
        connection_result = postgre_con(Database, Host, PORT, Username,
                                        Password)
    else:
        print(
            "Please Check your DB_type. This only input 'oracle', 'db2', 'sql server', 'postgre'"
        )

    return connection_result
