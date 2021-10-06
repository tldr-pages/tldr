# lsd

> List directory contents.
> The next generation `ls` command, written in Rust.
> More information: <https://github.com/Peltoche/lsd>.

- List files and directories, one per line:

`lsd -1`

- List all files and directories, including hidden ones, in the current directory:

`lsd -a`

- List all files and directories with trailing `/` added to directory names:

`lsd -F`

- List all files and directories in long format (permissions, ownership, size, and modification date):

`lsd -la`

- List all files and directories in long format with size displayed using human-readable units (KiB, MiB, GiB):

`lsd -lh`

- List all files and directories in long format, sorted by size (descending):

`lsd -lS`

- List all files and directories in long format, sorted by modification date (oldest first):

`lsd -ltr`

- Only list directories:

`lsd -d {{*/}}`
