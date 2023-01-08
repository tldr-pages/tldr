# fossil rm

> Remove files or directories from Fossil version control.
> See also `fossil forget`.
> More information: <https://fossil-scm.org/home/help/rm>.

- Remove a file or directory from Fossil version control:

`fossil rm {{path/to/file_or_directory}}`

- Remove a file or directory from Fossil version control, and also delete it from the disk:

`fossil rm --hard {{path/to/file_or_directory}}`

- Re-add all previously removed and uncommitted files to Fossil version control:

`fossil rm --reset`
