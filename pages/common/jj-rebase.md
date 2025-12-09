# jj rebase

> Move revisions to different parent(s).
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-rebase>.

- Move given revisions to a different parent(s):

`jj rebase {{[-r|--revisions]}} {{revset}} {{[-d|--destination]}} {{revset}}`

- Move given revisions and all their descendants:

`jj rebase {{[-s|--source]}} {{revset}} {{[-d|--destination]}} {{revset}}`

- Move all revisions in the branch containing given revisions:

`jj rebase {{[-b|--branch]}} {{revset}} {{[-d|--destination]}} {{revset}}`

- Move revisions to before and/or after other revisions:

`jj rebase {{[-r|--revisions]}} {{revset}} {{[-B|--insert-before]}} {{revset}} {{[-A|--insert-after]}} {{revset}}`
