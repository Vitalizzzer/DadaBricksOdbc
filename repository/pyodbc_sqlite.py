import sqlite3

import data.query as query
import logging


def open_connection():
    return sqlite3.connect('resources/testdb.db')


def create_table(connection, table_name):
    c = connection.cursor()
    if check_table_exists(connection, table_name):
        c.execute(query.DROP_TABLE.format(table_name))
    c.execute(query.CREATE_TABLE_QUERY.format(table_name))
    connection.commit()


def insert(connection, table_name, value1, value2):
    c = connection.cursor()
    c.execute(query.INSERT_QUERY.format(table_name), {'first': value1, 'last': value2})
    connection.commit()


def update(connection, table_name, new_value1, new_value2, old_value1):
    c = connection.cursor()
    c.execute(query.UPDATE_QUERY.format(table_name, new_value1, new_value2, old_value1))
    connection.commit()


def delete(connection, table_name, value1, value2):
    c = connection.cursor()
    c.execute(query.DELETE_QUERY.format(table_name, value1, value2))
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


def select_specific(connection, table_name, value1, value2):
    c = connection.cursor()
    c.execute(query.SELECT_SPECIFIC_QUERY.format(table_name, value1, value2))
    result = c.fetchall()
    logging.info(f'Query result size: {len(result)}\n')
    return result
