# psalm

> A static analysis tool for finding errors in PHP applications.
> More information: <https://psalm.dev>.

- Generate a Psalm configuration:

`psalm --init`

- Analyse the current working directory:

`psalm`

- Analyse a specific directory or file:

`psalm {{path/to/file_or_directory}}`

- Analyse a project with a specific configuration file:

`psalm --config {{path/to/psalm.xml}}`

- Include informational findings in the output:

`psalm --show-info`

- Analyse a project and display statistics:

`psalm --stats`

- Analyse a project in parallel with 4 threads:

`psalm --threads {{4}}`
