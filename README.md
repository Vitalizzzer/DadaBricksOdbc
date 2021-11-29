### ODBC Testing POC
The test suite executed ODBC tests with Sqlite database

### Prerequisites
Add environment variables for Report Portal in terminal:
export RP_TOKEN=<TOKEN>
export RP_ENDPOINT=<REPORT_PORTAL_ADDRESS>
export RP_PROJECT=<PROJECT_NAME>

### Execution
Run in terminal:
```bash 
behave -D rp_enable=True -D step_based=True --tags=ODBC 
```