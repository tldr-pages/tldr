# fossil delete

> Remove files or directories from Fossil version control.
> See also: `fossil forget`.
> More information: <https://fossil-scm.org/home/help/delete>.

- Remove a file or directory from Fossil version control:

`fossil {{[rm|delete]}} {{path/to/file_or_directory}}`

- Remove a file or directory from Fossil version control, and also delete it from the disk:

`fossil {{[rm|delete]}} --hard {{path/to/file_or_directory}}`

- Re-add all previously removed and uncommitted files to Fossil version control:

`fossil {{[rm|delete]}} --reset`
