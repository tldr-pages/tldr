# jj new

> Create a new empty change.
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-new>.

- Create a new empty change on top of current revision:

`jj new`

- Create a new empty change on top of specific revision:

`jj new {{revision}}`

- Create a new merge change on top of multiple revisions:

`jj new {{revset1 revset2 ...}}`

- Create a new empty change before and after specified revisions:

`jj new {{[-B|--insert-before]}} {{revsets}} {{[-A|--insert-after]}} {{revsets}}`
