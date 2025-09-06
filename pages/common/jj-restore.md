# jj restore

> Restore files from another revision.
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-restore>.

- Restore files from a revision into another revision:

`jj restore {{[-f|--from]}} {{revset}} {{[-t|--into]}} {{revset}} {{filesets}}`

- Undo the changes in a revision as compared to the merge of its parents:

`jj restore {{[-c|--changes-in]}} {{revset}} {{filesets}}`

- Interactively choose what parts to restore:

`jj restore {{[-f|--from]}} {{revset}} {{[-t|--into]}} {{revset}} {{[-i|--interactive]}}`
