# df

> Gives an overview of the file system disk space usage.

- Display all file systems and their disk usage:

`df`

- Display all file systems and their disk usage in human readable form:

`df -h`

- Display the file system and its disk usage containing the given file or directory:

`df {{path/to/file_or_directory}}`

- Display statistics on the number of free inodes:

`df -i`

- Display file systems but exclude the specified type:

`df -x {{squashfs}} -x {{tmpfs}}`
