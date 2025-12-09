# jj next

> Move the working-copy commit to a child revision.
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-next>.

- Move the working-copy commit to the next child revision:

`jj next`

- Move the working-copy commit a number of revisions forward:

`jj next {{offset}}`

- Edit the child revision directly, instead of creating a new working-copy commit:

`jj next {{[-e|--edit]}}`

- Create a new working-copy commit instead of editing the child revision directly:

`jj next {{[-n|--no-edit]}}`

- Jump to the next conflicted child:

`jj next --conflict`
