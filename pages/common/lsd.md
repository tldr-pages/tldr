# lsd

> List directory contents.
> More information: <https://github.com/Peltoche/lsd>.

- List files and directories, one per line.

`lsd -1`

- List all files, including hidden files:

`lsd -a`

- List all files and directories, with trailing `/` added to directory names:

`lsd -F`

- Long format list (permissions, ownership, size, and modification date) of all files:

`lsd -la`

- Long format list with size displayed using human-readable units (KiB, MiB, GiB):

`lsd -lh`

- Long format list sorted by size (descending):

`lsd -lS`

- Long format list of all files, sorted by modification date (oldest first):

`lsd -ltr`

- Only list directories:

`lsd -d {{*/}}`
