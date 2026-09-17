# jj file show

> Print contents of files in a revision of a `jj` repository.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-file-show>.

- Print the contents of a file in the working copy:

`jj file show {{path/to/file}}`

- Print the contents of a file in a specific revision:

`jj file show {{[-r|--revision]}} {{revision}} {{path/to/file}}`

- Print all files under a directory recursively:

`jj file show {{path/to/directory}}`

- Print file metadata using a custom template:

`jj file show {{[-T|--template]}} "{{template}}" {{path/to/file}}`
