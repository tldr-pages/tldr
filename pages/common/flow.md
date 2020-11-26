# flow

> A static type checker for JavaScript.
> More information: <https://flow.org>.

- Run flow check:

`flow`

- Check which files are being checked by flow:

`flow ls`

- Run type coverage check on all files in a directory:

`flow batch-coverage --show-all --strip-root {{path/to/directory}}`

- Display line-by-line stats on type coverage:

`flow coverage --color {{path/to/file.jsx}}`
