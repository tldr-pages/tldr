# zipnote

> View, add, or edit a zip archive's comments.
> Files can also be renamed in the zip archive.
> More information: <https://linux.die.net/man/1/zipnote>.

- View the comments on a zip archive:

`zipnote {{path/to/file.zip}}`

- Extract the comments on a zip archive to a file:

`zipnote {{path/to/file.zip}} > {{path/to/file.txt}}`

- Add/Update comments/filename in zip archive from a temporary file:

`zipnote -w {{path/to/file.zip}} < {{path/to/file.txt}}`
