# df

> Display an overview of the filesystem disk space usage.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/df-invocation.html>.

- Display all filesystems and their disk usage:

`df`

- Display all filesystems and their disk usage in human-readable form:

`df {{[-h|--human-readable]}}`

- Display the filesystem and its disk usage containing the given file or directory:

`df {{path/to/file_or_directory}}`

- Include statistics on the number of free inodes:

`df {{[-i|--inodes]}}`

- Display filesystems but exclude the specified types:

`df {{[-x|--exclude-type]}} {{squashfs}} {{[-x|--exclude-type]}} {{tmpfs}}`

- Display filesystem types:

`df {{[-T|--print-type]}}`
