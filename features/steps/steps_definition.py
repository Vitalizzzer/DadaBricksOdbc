from behave import *
import business_logic.pyodbc_sqlite as bl


@given('table name "{table_name}"')
def provided_table_name(context, table_name):
    context.table_name = table_name
    bl.create_table(context.connection, context.table_name)


@when('insert first name {firstname} and last name {lastname}')
def insert_first_name_and_last_name(context, firstname, lastname):
    bl.insert_data(context.connection, context.table_name, firstname, lastname)


@then('correct data with {firstname} and {lastname} appears in the database')
def correct_data_appears_in_db(context, firstname, lastname):
    result = bl.select_all(context.connection, context.table_name)
    for value in result:
        assert firstname == value[0], "Could not find value {}. Actual: {}".format(firstname, value[0])
        assert lastname == value[1], "Could not find value {}. Actual: {}".format(lastname, value[1])
