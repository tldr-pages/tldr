# jj fix

> Update files with formatting fixes or other content transformations.
> Revisions can be reviewed afterwards with `jj op show -p`.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-fix>.

- Fix changed files in all mutable revisions connected to the working-copy commit:

`jj fix`

- Fix changed files in the specified revision(s) and their descendants:

`jj fix {{[-s|--source]}} {{revsets}}`

- Fix files only in the working-copy commit:

`jj fix {{[-s|--source]}} @`

- Fix only a specific file or directory:

`jj fix {{path/to/file_or_directory}}`

- Fix all lines instead of only modified lines:

`jj fix {{[-a|--all-lines]}}`

- Format all lines in a specific file:

`jj fix {{[-a|--all-lines]}} {{path/to/file}}`

- Fix unchanged files in addition to changed ones across the entire repository:

`jj fix --include-unchanged-files`

- Fix unchanged files in addition to changed ones for specific paths:

`jj fix --include-unchanged-files {{path/to/file_or_directory}}`
