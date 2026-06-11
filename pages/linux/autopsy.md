# autopsy

> Digital forensics platform for analyzing disk images and investigating file systems.
> More information: <https://www.autopsy.com>.

- Launch the Autopsy graphical interface:

`autopsy`

- Create a new case and specify the base directory to store case files:

`autopsy --createCase --caseName {{case_name}} --caseBaseDir {{path/to/base_directory}}`

- Add a data source to an existing case:

`autopsy --caseBaseDir {{path/to/base_directory}} --caseName {{case_name}} --addDataSource --dataSourcePath {{path/to/image.dd}}`

- Add a data source to an existing case and immediately run ingest modules:

`autopsy --caseBaseDir {{path/to/base_directory}} --caseName {{case_name}} --addDataSource --dataSourcePath {{path/to/image.dd}} --runIngest`

- Generate a report for an existing case using a reports profile:

`autopsy --caseBaseDir {{path/to/base_directory}} --caseName {{case_name}} --generateReports={{profile_name}}`

- List all data sources in an existing case:

`autopsy --caseBaseDir {{path/to/base_directory}} --caseName {{case_name}} --listAllDataSources`
