# zipnote

> View, add, or edit a Zip archive's comments.
> Files can also be renamed in the Zip archive.
> More information: <https://manned.org/zipnote>.

- View the comments on a Zip archive:

`zipnote {{path/to/file.zip}}`

- Extract the comments on a Zip archive to a file:

`zipnote {{path/to/file.zip}} > {{path/to/file.txt}}`

- Add/Update comments in a Zip archive from a file:

`zipnote -w {{path/to/file.zip}} < {{path/to/file.txt}}`
