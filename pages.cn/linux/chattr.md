# chattr

> Change attributes of files or folders.

- Make a file or folder immutable to changes and deletion, even by superuser:

`chattr +i {{path}}`

- Make a file or folder mutable:

`chattr -i {{path}}`

- Recursively make an entire folder and contents immutable:

`chattr -R +i {{folder}}`
