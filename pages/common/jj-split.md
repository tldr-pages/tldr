# jj split

> Split a revision in two.
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-split>.

- Split the given revision into two interactively, putting the second revision on top of it:

`jj split {{[-r|--revision]}} {{revision}}`

- Split out matching files from the given revision:

`jj split {{[-r|--revision]}} {{revision}} {{fileset}}`

- Split the given revision, putting the second revision on top of given destination(s):

`jj split {{[-r|--revision]}} {{revision}} {{[-d|--destination]}} {{revset}}`

- Split the given revision, putting the second revision before and/or after other revision(s):

`jj split {{[-r|--revision]}} {{revision}} {{[-B|--insert-before]}} {{revset}} {{[-A|--insert-after]}} {{revset}}`

- Split the given revision into two parallel revisions:

`jj split {{[-r|--revision]}} {{revision}} {{[-p|--parallel]}}`
