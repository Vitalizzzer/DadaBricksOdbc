@ODBC
#noinspection CucumberUndefinedStep,CucumberPlusUndefinedStep
Feature: Database CRUD commands and data verification
  CRUD commands are executed and results are verified

  Background:
    Given table name "employee"

  @1 @TestCaseKey=TGTB-T1
  Scenario Outline: Insert and verify data
    When insert first name <FirstName> and last name <LastName>
    Then correct data with <FirstName> and <LastName> appears in the database

    Examples:
      | FirstName | LastName |
      | Vitalii   | Rymar    |

#  @2
#  Scenario Outline: Update and verify data
#    When insert first name <FirstName> and last name <LastName>
#    Then correct data with <FirstName> and <LastName> appears in the database
#    When update data with <NewFirstName> and <NewLastName> where first name = <FirstName>
#    Then correct data with <NewFirstName> and <NewLastName> appears in the database
#
#    Examples:
#      | FirstName | LastName | NewFirstName | NewLastName |
#      | Vitalii   | Rymar    | John         | Smith       |
#
#  @3
#  Scenario Outline: Delete and verify data
#    When insert first name <FirstName> and last name <LastName>
#    Then correct data with <FirstName> and <LastName> appears in the database
#    When delete data where first name = <FirstName> and last name = <LastName>
#    Then data is absent with <FirstName> and <LastName>
#
#    Examples:
#      | FirstName | LastName |
#      | Vitalii   | Rymar    |