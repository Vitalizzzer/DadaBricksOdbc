import sqlite3

import data.query as query


def open_connection():
    return sqlite3.connect('resources/testdb.db')


def create_table(connection, table_name):
    c = connection.cursor()
    if check_table_exists(connection, table_name):
        c.execute(query.DROP_TABLE.format(table_name))
    c.execute(query.CREATE_TABLE_QUERY.format(table_name))
    connection.commit()


def insert_data(connection, table_name, value1, value2):
    c = connection.cursor()
    c.execute(query.INSERT_DATA_QUERY.format(table_name), {'first': value1, 'last': value2})
    connection.commit()


def check_table_exists(connection, table_name):
    c = connection.cursor()
    c.execute(query.SELECT_TABLE_EXISTS.format(table_name))
    row = c.fetchone()
    if row is None:
        return False
    return True


def select_all(connection, table_name):
    c = connection.cursor()
    c.execute(query.SELECT_ALL_QUERY.format(table_name))
    result = c.fetchall()
    return result
