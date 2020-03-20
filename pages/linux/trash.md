# trash

> A CLI for managing your trashcan / recycling bin.
> More information: <https://github.com/andreafrancia/trash-cli>.

- Delete a file (send to trash):

`trash {{path/to/file}}`

- List files in trash:

`trash-list`

- Restore file from trash:

`trash-restore`

- Empty trash:

`trash-empty`

- Empty trash, keeping files trashed less than {{10}} days ago:

`trash-empty {{10}}`

- Remove all files named 'foo' from the trash:

`trash-rm foo`

- Remove all files with a given original location:

`trash-rm /full/path`
