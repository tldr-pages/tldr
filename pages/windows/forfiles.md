# forfiles

> Select one or more files to execute a specified command on.

- Search for files in the current directory:

`forfiles`

- Search for files in a specific directory:

`forfiles /p {{path/to/directory}}`

- Run the specified command for each file:

`forfiles /c "{{command}}"`

- Search for files using a specific glob mask:

`forfiles /m {{glob_pattern}}`

- Search for files recursively:

`forfiles /s`

- Search for files older than 5 days:

`forfiles /d {{+5}}`
