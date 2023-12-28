# df

> Gives an overview of the filesystem disk space usage.
> More information: <https://keith.github.io/xcode-man-pages/df.1.html>.

- Display all filesystems and their disk usage using 512-byte units:

`df`

- Display all filesystems and their disk usage in human-readable form (based on powers of 1024):

`df -h`

- Display all filesystems and their disk usage in human-readable form (based on powers of 1000):

`df --si|-H`

- Display the filesystem and its disk usage containing the given file or directory:

`df {{path/to/file_or_directory}}`

- Include statistics on the number of free and used [i]nodes including the filesystem [T]ypes:

`df -iT`

- Use 1024-byte units when writing space figures:

`df -k`

- Display information in a portable way:

`df -P`
