# dir

> Dir is equivalent to ls -C -b; that is, by default files are listed in columns, sorted vertically, and special characters are represented by backslash escape sequences.
> More information: <https://manned.org/dir>.

- List all files, including hidden files:

`dir -all`

- List files including the author (`-l` is required):

`dir -l --author`

- List files excluding those that match a specified pattern:

`dir --hide={{pattern}}`

- List subdirectories recursively:

`dir --recursive`

- Display help:

`dir --help`
