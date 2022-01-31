from behave import *
import repository.pyodbc_sqlite as bl


@given('table name "{table_name}"')
def provided_table_name(context, table_name):
    context.table_name = table_name
    bl.create_table(context.connection, context.table_name)


@when('insert first name {firstname} and last name {lastname}')
def insert_first_name_and_last_name(context, firstname, lastname):
    bl.insert(context.connection, context.table_name, firstname, lastname)


@when('update data with {new_firstname} and {new_lastname} where first name = {old_firstname}')
def update_data(context, new_firstname, new_lastname, old_firstname):
    bl.update(context.connection, context.table_name, new_firstname, new_lastname, old_firstname)


@when('delete data where first name = {firstname} and last name = {lastname}')
def delete_data(context, firstname, lastname):
    bl.delete(context.connection, context.table_name, firstname, lastname)


@then('correct data with {firstname} and {lastname} appears in the database')
def correct_data_appears_in_db(context, firstname, lastname):
    result = bl.select_specific(context.connection, context.table_name, firstname, lastname)
    assert len(result) >= 1, "Select response is empty"

    for value in result:
        assert firstname == value[0], "Could not find value {}. Actual: {}".format(firstname, value[0])
        assert lastname == value[1], "Could not find value {}. Actual: {}".format(lastname, value[1])


@then('data is absent with {firstname} and {lastname}')
def data_is_absent(context, firstname, lastname):
    result = bl.select_specific(context.connection, context.table_name, firstname, lastname)
    for value in result:
        assert firstname != value[0], "Unexpected value {} is present. Expected: None".format(firstname)
        assert lastname != value[1], "Unexpected value {} is present. Expected: None".format(lastname)
