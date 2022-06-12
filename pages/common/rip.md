# rip

> Remove files or directories by sending them to the graveyard, allowing for them to be recovered.
> More information: <https://github.com/nivekuil/rip>.

- Remove files or directories from specified locations and place them in the graveyard:

`rip {{path/to/file_or_directory}} {{path/to/another/file_or_directory}}`

- Interactively remove files or directories, with a prompt before every removal:

`rip -i {{path/to/file_or_directory}} {{path/to/another/file_or_directory}}`

- List all files in the graveyard that were somewhere in the current directory:

`rip -s`

- Permanently delete every file and directory in the graveyard:

`rip -d`

- Undo the last removal:

`rip -u`

- Undo all removals that are listed by `rip -s`:

`rip -su`
