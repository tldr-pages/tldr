# df

> Display an overview of the filesystem disk space usage.
> More information: <https://man.freebsd.org/cgi/man.cgi?df>.

- Display all filesystems and their disk usage (using 512-byte units):

`df`

- Use [h]uman-readable units (based on powers of 1024) and display a grand total:

`df -h -c`

- Use [H]uman-readable units (based on powers of 1000):

`df -{{-si|H}}`

- Display the filesystem containing the specified file or directory:

`df {{path/to/file_or_directory}}`

- Include statistics on the number of free and used [i]nodes, including the filesystem [T]ypes:

`df -iT`

- Use 1024-byte units when showing size figures:

`df -k`

- Display information in a [P]ortable way:

`df -P`
