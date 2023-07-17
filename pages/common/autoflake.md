# autoflake

> A tool to remove unused imports and variables from Python code.
> More information: <https://github.com/myint/autoflake>.

- Remove unused variables from a single file and display the diff:

`autoflake --remove-unused-variables {{path/to/file.py}}`

- Remove unused imports from multiple files and display the diffs:

`autoflake --remove-all-unused-imports {{path/to/file1.py path/to/file2.py ...}}`

- Remove unused variables from a file, overwriting the file:

`autoflake --remove-unused-variables --in-place {{path/to/file.py}}`

- Remove unused variables recursively from all files in a directory, overwriting each file:

`autoflake --remove-unused-variables --in-place --recursive {{path/to/directory}}`
