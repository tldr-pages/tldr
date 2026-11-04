# jj arrange

> Interactively arrange the commit graph.
> See also: `jj rebase`, `jj squash`.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-arrange>.

- Interactively arrange commits configured by `revsets.arrange` (defaults to mutable commits):

`jj arrange`

- Interactively arrange specific revisions:

`jj arrange {{[-r|--revisions]}} {{revset}}`

- Interactively arrange multiple revsets:

`jj arrange {{[-r|--revisions]}} {{revset1}} {{[-r|--revisions]}} {{revset2}}`

- Interactively arrange a stack of commits from `trunk` to the current revision:

`jj arrange {{[-r|--revisions]}} 'trunk()..@'`
