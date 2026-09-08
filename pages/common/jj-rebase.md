# jj rebase

> Move revisions to different parent(s).
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-rebase>.

- Move given revisions to a different parent(s):

`jj rebase {{[-r|--revisions]}} {{revset}} {{[-o|--onto]}} {{revset}}`

- Move given revisions and all their descendants:

`jj rebase {{[-s|--source]}} {{revset}} {{[-o|--onto]}} {{revset}}`

- Move all revisions in the branch containing given revisions:

`jj rebase {{[-b|--branch]}} {{revset}} {{[-o|--onto]}} {{revset}}`

- Move revisions to before and/or after other revisions:

`jj rebase {{[-r|--revisions]}} {{revset}} {{[-B|--insert-before]}} {{revset}} {{[-A|--insert-after]}} {{revset}}`
