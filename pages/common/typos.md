# typos

> Find and correct spelling mistakes in source code.
> More information: <https://github.com/crate-ci/typos/blob/master/docs/reference.md>.

- Check a file or directory for spelling mistakes:

`typos {{path/to/file_or_directory}}`

- Automatically fix the typos in a file or directory:

`typos --write-changes {{path/to/file_or_directory}}`

- Preview the changes before actually applying them:

`typos --diff {{path/to/file_or_directory}}`

- List all supported file types:

`typos --type-list`

- Show spelling mistakes in a specific output format:

`typos --format {{brief|long|json}} {{path/to/file_or_directory}}`
