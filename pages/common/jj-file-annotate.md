# jj file annotate

> Show the source change for each line of a target file in a `jj` repository.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-file-annotate>.

- Annotate a file line by line in the working copy:

`jj file annotate {{path/to/file}}`

- Annotate a file starting at a specific revision:

`jj file annotate {{[-r|--revision]}} {{revision}} {{path/to/file}}`

- Annotate a file using a custom template:

`jj file annotate {{[-T|--template]}} "{{template}}" {{path/to/file}}`
