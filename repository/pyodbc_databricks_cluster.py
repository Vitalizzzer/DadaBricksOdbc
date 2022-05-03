import logging
from databricks import sql
import query.query as query


def open_connection(context):
    return sql.connect(server_hostname=f"{context.server_hostname}",
                       http_path=f"{context.http_path}",
                       access_token=f"{context.access_token}")


def create_table(connection, table_name, csv_file_path):
    c = connection.cursor()
    c.execute(query.DROP_TABLE.format(table_name))
    c.execute(query.CREATE_TABLE.format(table_name, csv_file_path))
    connection.commit()


def select_all(connection, table_name):
    c = connection.cursor()
    c.execute(query.SELECT_ALL_QUERY.format(table_name))
    result = c.fetchall()
    logging.info(f'Response: {result}\n')
    return result


def select_duplicates(connection, table_name):
    c = connection.cursor()
    c.execute(query.SELECT_DUPLICATES.format(table_name))
    result = c.fetchone()
    logging.info(f'Response: {result}\n')
    return result


def select_null_values(connection, table_name):
    c = connection.cursor()
    c.execute(query.SELECT_NULL_VALUES.format(table_name))
    result = c.fetchone()
    logging.info(f'Response: {result}\n')
    return result
