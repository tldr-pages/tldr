# loc

> Tool written in Rust that counts lines of code.

- Print lines of code in the current directory:

`loc`

- Print lines of code in the target directory:

`loc {{path/to/directory}}`

- Print lines of code with stats for individual files:

`loc --files`

- Print lines of code without .gitignore (etc.) files (e.g. two -u flags will additionally count hidden files and dirs):

`loc -u`
