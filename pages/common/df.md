# df

> Display an overview of the filesystem disk space usage.
> More information: <https://manned.org/df.1posix>.

- Display all filesystems and their disk usage (using 512-byte units):

`df`

- Display the filesystem containing the specified file or directory:

`df {{path/to/file_or_directory}}`

- Use [k]ibibyte (1024 byte) units when showing size figures:

`df -k`

- Display information in a portable way:

`df -P`
