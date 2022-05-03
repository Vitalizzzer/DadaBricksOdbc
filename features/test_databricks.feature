@ODBC
#noinspection CucumberUndefinedStep,CucumberPlusUndefinedStep
Feature: Database CRUD commands and data verification in Azure Databricks
  CRUD commands are executed and results are verified

  Background:
    #Given uploaded file "resources/data/csv/products.csv"
    Given created table name "products" from file "/FileStore/tables/products.csv"

  @1
  Scenario: Verify absent duplications
    Then number of duplications is "0"

  @1
  Scenario: Verify absent NULL values
    Then number of NULL values is "0"
