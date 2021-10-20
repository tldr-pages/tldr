# fossil add

> Put files or directories under Fossil version control.
> More information: <https://fossil-scm.org/home/help/add>.

- Add files or directories to the current checkout at the next commit:

`fossil add {{path/to/file_or_directory}}`

- Reset the add state of a checkout such that newly added but not committed files are no longer added; that is, undo uncommitted add command(s):

`fossil add --reset`
