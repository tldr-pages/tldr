# df

> Display an overview of the filesystem disk space usage.
> More information: <https://pubs.opengroup.org/onlinepubs/9699919799.2018edition/utilities/df.html>.

- Display all filesystems and their disk usage using 512-byte units:

`df`

- Display the filesystem and its disk usage containing the given file or directory:

`df {{path/to/file_or_directory}}`

- Use 1024-byte units when writing space figures:

`df -k`

- Display information in a portable way:

`df -P`
