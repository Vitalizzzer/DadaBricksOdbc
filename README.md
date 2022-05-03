# ODBC Testing MVP

The test suite executes ODBC tests in Azure Databricks.

## Configuration

###Add environment variables for Azure Databricks in terminal:
```
export SERVER_HOSTNAME=<SERVER_HOSTNAME>
export HTTP_PATH=<HTTP_PATH>
export ACCESS_TOKEN=<ACCESS_TOKEN>
```

###Add environment variables for Report Portal in terminal (optional):
```
export RP_UUID=<UUID>
export RP_ENDPOINT=<REPORT_PORTAL_ADDRESS>
export RP_PROJECT=<PROJECT_NAME>
export RP_LAUNCH=<LAUNCH_NAME>
```

## Execution
### Run the command in the terminal:

* With html report:
```bash 
behave -f html -o report/cucumber_report.html -D rp_enable=False -D step_based=True --tags=ODBC
```

* With json report:
```bash 
behave -f json.pretty -o report/cucumber_report.json -D rp_enable=False -D step_based=True --tags=ODBC
```

***Note:*** to enable publishing results to Report Portal set ```rp_enable=True``` in the command above.

## Reporting
Execution results are in ***report/cucumber_report.html*** or ***report/cucumber_report.json***

## TODO: 
1. Implement REST requests to inject and delete test data files in Azure Databricks 
2. Implement trigger scripts execution in Azure Databricks and extract report.