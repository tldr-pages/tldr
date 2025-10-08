# df

> Display an overview of the filesystem disk space usage.
> More information: <https://man.openbsd.org/df.1>.

- Display all filesystems and their disk usage (using 512-byte units):

`df`

- Display all filesystems in [h]uman-readable form (based on powers of 1024):

`df -h`

- Display the filesystem containing the specified file or directory:

`df {{path/to/file_or_directory}}`

- Include statistics on the number of free and used [i]nodes:

`df -i`

- Use [k]ibibyte (1024 byte) units when showing size figures:

`df -k`

- Display information in a [P]ortable way:

`df -P`
