# fossil rm

> Remove files or directories from Fossil version control.
> Can alternatively be called as `fossil delete` or `fossil forget`.
> More information: <https://fossil-scm.org/home/help>.

- Remove files or directories from Fossil version control:

`fossil rm {{path/to/file_or_directory}}`

- Remove files or directories from Fossil version control, also deleting the files or directories from the local checkout:

`fossil rm --hard {{path/to/file_or_directory}}`

- Reset the deleted state of a checkout such that newly rm'd but not committed files are no longer deleted; that is, undo uncommitted rm command(s):

`fossil rm --reset`
