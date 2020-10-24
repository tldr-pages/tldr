# scc

> Tool written in Go that counts lines of code.
> More information: <https://github.com/boyter/scc>.

- Print lines of code in the current directory:

`scc`

- Print lines of code in the target directory:

`scc {{path/to/directory}}`

- Display output for every file:

`scc --by-file`

- Display output using a specific output format (defaults to `tabular`):

`scc --format {{tabular|wide|json|csv|cloc-yaml|html|html-table}}`

- Only count files with specific file extensions:

`scc --include-ext {{go, java, js}}`

- Exclude directories from being counted:

`scc --exclude-dir {{.git,.hg}}`

- Display output and sort by column (defaults to by files):

`scc --sort {{files|name|lines|blanks|code|comments|complexity}}`

- Print help for scc:

`scc -h`
