# jj file list

> List files in a revision of a `jj` repository.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-file-list>.

- List all files in the current working copy:

`jj file list`

- List all files in a specific revision:

`jj file list {{[-r|--revision]}} {{revision}}`

- List files matching a specific prefix or path:

`jj file list {{path/to/directory}}`

- List files rendered using a custom template:

`jj file list {{[-T|--template]}} "{{template}}"`
