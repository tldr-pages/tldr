# dir

> List directory contents using one line per file, special characters are represented by backslash escape sequences.
> Works as `ls -C --escape`.
> More information: <https://manned.org/dir>.

- List all files, including hidden files:

`dir -all`

- List files including their author (`-l` is required):

`dir -l --author`

- List files excluding those that match a specified blob pattern:

`dir --hide={{pattern}}`

- List subdirectories recursively:

`dir --recursive`

- Display help:

`dir --help`
