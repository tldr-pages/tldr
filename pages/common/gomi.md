# gomi

> Manage the trashcan.
> See also: `trash`, `rm`.
> More information: <https://github.com/babarot/gomi>.

- Delete safely specific files or folders (no need for flag `-rf`):

`gomi {{path/to/file1 path/to/folder ...}}`

- Restore one or more files, going back:

`gomi {{[-b|--restore]}}`

- Remove files older than a specific time (day, week, month, year):

`gomi --prune={{1d|1w|1m|1y|...}}`

- Remove orphaned `.trashinfo` files (which contain the info of the deleted files, when thay have been deleted and where, a metadata file, that is abandoned and not useful anymore):

`gomi --prune={{orphans}}`
