# jj evolog

> Show how a change has evolved over time, listing the previous commits it has pointed to.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-evolog>.

- Show how a revision has evolved over time:

`jj evolog {{[-r|--revisions]}} {{revsets}}`

- Show diff statistics in the evolution log:

`jj evolog {{[-r|--revisions]}} {{revsets}} --stat`

- Show summary of each change in the evolution log:

`jj evolog {{[-r|--revisions]}} {{revsets}} {{[-s|--summary]}}`
