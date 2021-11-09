from loguru import logger

from business_logic.pyodbc_sqlite import open_connection


def before_all(context):
    context.config.setup_logging()


def before_scenario(context, scenario):
    context.connection = open_connection()
    logger.info("Connection is opened")


def after_scenario(context, scenario):
    context.connection.close()
    logger.info("Connection is closed")
