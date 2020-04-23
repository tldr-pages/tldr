# chattr

> Change attributes of files or directories.

- Make a file or directory immutable to changes and deletion, even by superuser:

`chattr +i {{path/to/file_or_directory}}`

- Make a file or directory mutable:

`chattr -i {{path/to/file_or_directory}}`

- Recursively make an entire directory and contents immutable:

`chattr -R +i {{path/to/directory}}`
