# gitty

> Minimal Git and GitHub CLI wrapper with human-readable commands.
> More information: <https://github.com/Omibranch/gitty>.

- Stage all changes, commit with an auto-generated message, and push:

`gitty up`

- Stage all changes and commit with a custom message:

`gitty up "{{commit message}}"`

- Show a compact, decorated git log:

`gitty log`

- Restore a specific file to its state before uncommitted changes:

`gitty fix {{file}}`

- Remove a file or path from all past commits permanently:

`gitty erase {{path_or_file}}`

- Undo the latest N commits (keeps changes staged):

`gitty back {{n}}`
