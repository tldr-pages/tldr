# chattr

> Change attributes of files or directories.
> More information: <https://manned.org/chattr>.

- Make a file or directory [i]mmutable to changes and deletion, even by superuser:

`chattr +i {{path/to/file_or_directory}}`

- Make a file or directory mutable:

`chattr -i {{path/to/file_or_directory}}`

- [R]ecursively make an entire directory and contents immutable:

`chattr -R +i {{path/to/directory}}`

- Mark a directory and its files to be interpreted in a case-insensitive manner:

`chattr +F {{path/to/directory}}`

- Set a file to only allow [a]ppending:

`chattr +a {{path/to/file}}`
