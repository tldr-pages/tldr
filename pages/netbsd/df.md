# df

> Display an overview of the filesystem disk space usage.
> More information: <https://man.netbsd.org/NetBSD-9.3/df.1>.

- Display all filesystems and their disk usage using 512-byte units:

`df`

- Use [h]uman-readable units (based on powers of 1024):

`df -h`

- Display all the fields of the structure(s) returned by `statvfs`:

`df -G`

- Display the filesystem and its disk usage containing the given file or directory:

`df {{path/to/file_or_directory}}`

- Include statistics on the number of free and used [i]nodes:

`df -i`

- Use 1024-byte units when writing space figures:

`df -k`

- Display information in a [P]ortable way:

`df -P`
