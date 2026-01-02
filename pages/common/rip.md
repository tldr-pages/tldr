# rip

> Remove files or directories by sending them to the graveyard, allowing for them to be recovered.
> More information: <https://github.com/nivekuil/rip#-usage>.

- Remove files or directories from specified locations and place them in the graveyard:

`rip {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Interactively remove files or directories, with a prompt before every removal:

`rip {{[-i|--inspect]}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- List all files and directories in the graveyard that were originally within the current directory:

`rip {{[-s|--seance]}}`

- Permanently delete every file and directory in the graveyard:

`rip {{[-d|--decompose]}}`

- Put back the files and directories which were affected by the most recent removal:

`rip {{[-u|--unbury]}}`

- Put back every file and directory that is listed by `rip --seance`:

`rip {{[-s|--seance]}} {{[-u|--unbury]}}`
