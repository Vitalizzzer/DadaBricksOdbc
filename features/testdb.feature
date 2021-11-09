Feature: test data base main functions

  Scenario Outline: insert and verify data
    Given table name "employee"
    When insert first name <FirstName> and last name <LastName>
    Then correct data with <FirstName> and <LastName> appears in the database

    Examples:
      | FirstName | LastName |
      | Vitalii   | Rymar    |