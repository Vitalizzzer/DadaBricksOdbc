import logging
from behave import *
import repository.pyodbc_databricks_cluster as databricks

logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')


@given('uploaded file "{local_file_path}"')
def uploaded_file(context, local_file_path):
    databricks.create_table(context.connection, context.table_name, local_file_path)


@given('created table name "{table_name}" from file "{file_path}"')
def created_table_name_from_csv(context, table_name, file_path):
    context.table_name = table_name
    databricks.create_table(context.connection, context.table_name, file_path)


@when('select all query from table "{table_name}"')
def select_all_data(context, table_name):
    databricks.select_all(context.connection, table_name)


@then('number of duplications is "{duplicates_number}"')
def number_of_duplications(context, duplicates_number):
    result = databricks.select_duplicates(context.connection, context.table_name)
    actual_duplicates = str(result["DuplicateRecords"])
    assert actual_duplicates == duplicates_number, "Number of duplicates is incorrect. Expected: {} Actual: {}"\
        .format(duplicates_number, actual_duplicates)


@then('number of NULL values is "{null_values_number}"')
def number_of_null_values(context, null_values_number):
    result = databricks.select_null_values(context.connection, context.table_name)
    actual_null_values = str(result["NullValues"])
    assert actual_null_values == null_values_number, "Number of NULL values is incorrect. Expected: {} Actual: {}"\
        .format(null_values_number, actual_null_values)
