# autopsy

> Digital forensics platform for analyzing disk images and investigating file systems.
> More information: <https://sleuthkit.org/autopsy/docs/user-docs/4.14.0/command_line_ingest_page.html>.

- Launch the Autopsy graphical interface:

`autopsy64.exe`

- Create a new case and specify the base directory to store case files:

`autopsy64.exe --createCase --caseName {{case_name}} --caseBaseDir {{path\to\base_directory}}`

- Add a data source to an existing case:

`autopsy64.exe --caseDir {{path\to\case_directory}} --addDataSource --dataSourcePath {{path\to\source}}`

- Generate a report for an existing case:

`autopsy64.exe --caseDir {{path\to\case_directory}} --generateReports`

- List all data sources in an existing case:

`autopsy64.exe --caseDir {{path\to\case_directory}} --listAllDataSources`
