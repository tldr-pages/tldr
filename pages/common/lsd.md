# lsd

> List directory contents.
> The next generation `ls` command, written in Rust.
> More information: <https://github.com/Peltoche/lsd>.

- List files and directories, one per line:

`lsd -1`

- List all files and directories, including hidden ones, in the current directory:

`lsd -a`

- List files and directories with trailing `/` added to directory names:

`lsd -F`

- List all files and directories in long format (permissions, ownership, size in human-readable format, and modification date):

`lsd -lha`

- List files and directories in long format, sorted by size (descending):

`lsd -lS`

- List files and directories in long format, sorted by modification date (oldest first):

`lsd -ltr`

- Only list directories:

`lsd -d {{*/}}`

- Recursively list all directories in a tree format:

`lsd --tree -d`
