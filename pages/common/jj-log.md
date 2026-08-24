# jj log

> Show revision history as a graph.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-log>.

- Show revision history as a graph:

`jj log`

- Show only given revsets (e.g. `B::D`, `A..D`, `B|C|D`, etc.):

`jj log {{[-r|--revisions]}} {{revsets}}`

- Show log with a particular template for each line (e.g. 5 characters of commit hash and author):

`jj log {{[-T|--template]}} 'commit_id.shortest(5) ++ " " ++ author'`
