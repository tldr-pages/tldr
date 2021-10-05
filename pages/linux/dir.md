# dir

> dir is equivalent to ls -C -b; that is, by default files are listed in columns, sorted vertically, and special characters are represented by backslash escape sequences.
> More information: https://www.geeksforgeeks.org/dir-command-in-linux-with-examples/.

- Displays all the hidden files along with two files denoted by "." and "..":

`dir -a`

- Similar to -a option except that it does not display files that signals the current directory and previous directory:

`dir -A`

- Displays author of all the files. -l is required to display the contents in the form of a list:

`dir -l --author`

- Ignores listing of backed up files. These files end with a "~":

`dir -B`

- Ignores files described by shell PATTERN while listing the contents of a directory:

`dir --hide=PATTERN`

- Similar to the long listing that is -l option except that it lists numeric user and group IDs:

`dir -n`

- List files in reverse order while sorting:

`dir -r`

- List subdirectories recursively.:

`dir -R`

- Display the help options and exit:

`dir --help`

- Outputs version information and exit:

`dir --version`

