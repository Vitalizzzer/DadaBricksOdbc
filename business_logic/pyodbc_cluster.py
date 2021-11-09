import pyodbc

# Replace <table-name> with the name of the database table to query.
table_name = "<table-name>"

# Connect to the Databricks cluster by using the
# Data Source Name (DSN) that you created earlier.

# conn = pyodbc.connect("DSN=Databricks_Cluster", autocommit=True)

conn = pyodbc.connect("Driver=<driver-path>;" +
                      "HOST=<server-hostname>;" +
                      "PORT=443;" +
                      "Schema=default;" +
                      "SparkServerType=3;" +
                      "AuthMech=3;" +
                      "UID=token;" +
                      "PWD=<personal-access-token>;" +
                      "ThriftTransport=2;" +
                      "SSL=1;" +
                      "HTTPPath=<http-path>",
                      autocommit=True)

# Run a SQL query by using the preceding connection.
cursor = conn.cursor()
cursor.execute(f"SELECT * FROM {table_name} LIMIT 2")

# Print the rows retrieved from the query.
print(f"Query output: SELECT * FROM {table_name} LIMIT 2\n")
for row in cursor.fetchall():
    print(row)
