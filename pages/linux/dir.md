
# dir

> Dir is equivalent to ls -C -b; that is, by default files are listed in columns, sorted vertically, and special characters are represented by backslash escape sequences.
> More information: <https://manned.org/dir>.

- Displays all the hidden files along with two files denoted by "." and "..":

`dir -a`

- Displays author of all the files. -l is required to display the contents in the form of a list:

`dir -l --author`

- Ignore files described by shell PATTERN while listing the contents of a directory:

`dir --hide=PATTERN`

- List subdirectories recursively.:

`dir -R`

- Display the help options and exit:

`dir --help`
