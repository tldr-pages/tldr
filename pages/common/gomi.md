# gomi

> Manage the trashcan.
> See also: `trash`, `rm`.
> More information: <https://github.com/babarot/gomi>.

- Safely delete specific files or folders:

`gomi {{path/to/file1 path/to/file2 path/to/folder1 path/to/folder2 ...}}`

- Open an interactive menu to restore one or more files:

`gomi {{[-b|--restore]}}`

- Remove files that have been in the trashcan longer than the specified time ([d]ay, [w]eek, [m]onth, [y]ear):

`gomi --prune {{1d|1w|1m|1y|...}}`

- Remove orphaned `.trashinfo` files:

`gomi --prune {{orphans}}`
