# jj file

> Manage and inspect files in a `jj` repository.
> Some subcommands such as `annotate`, `chmod`, `list`, `search`, `show`, `track`, `untrack` have their own usage documentation.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-file>.

- List files tracked in the working copy:

`jj file list`

- Print the contents of a file in the working copy:

`jj file show {{path/to/file}}`

- Search for a pattern across tracked files:

`jj file search {{[-p|--pattern]}} "{{pattern}}"`

- Show line-by-line source change annotation for a file:

`jj file annotate {{path/to/file}}`

- Track specified paths in the working copy:

`jj file track {{path/to/file_or_directory}}`

- Stop tracking specified paths in the working copy:

`jj file untrack {{path/to/file_or_directory}}`

- Set or remove the executable bit for a file:

`jj file chmod {{[-x|--executable]}} {{path/to/file}}`
