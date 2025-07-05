# jj evolog

> Show how a change has evolved over time, listing the previous commits it has pointed to.
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-evolog>.

- Show how a revision has evolved over time:

`jj evolog {{[-r|--revision]}} {{revset}}`

- Show diff statistics in the evolution log:

`jj evolog {{[-r|--revision]}} {{revset}} --stat`

- Show summary of each change in the evolution log:

`jj evolog {{[-r|--revision]}} {{revset}} {{[-s|--summary]}}`
