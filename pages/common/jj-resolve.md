# jj resolve

> Resolve conflicted files with an external merge tool.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-resolve>.

- Resolve all conflicts:

`jj resolve`

- List all conflicts:

`jj resolve {{[-l|--list]}}`

- Resolve conflicts in a given revision:

`jj resolve {{[-r|--revision]}} {{revset}}`

- Resolve conflicts in given files:

`jj resolve {{file1 file2 ...}}`

- Resolve accepting the incoming versions:

`jj resolve --tool :theirs`

- Resolve accepting the outgoing versions:

`jj resolve --tool :ours`
