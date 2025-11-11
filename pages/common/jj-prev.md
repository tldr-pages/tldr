# jj prev

> Move the working-copy commit to a parent revision.
> More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-prev>.

- Move the working-copy commit to the previous parent revision:

`jj prev`

- Move the working-copy commit a number of revisions backward:

`jj prev {{offset}}`

- Edit the parent revision directly, instead of creating a new working-copy commit:

`jj prev {{[-e|--edit]}}`

- Create a new working-copy commit instead of editing the parent revision directly:

`jj prev {{[-n|--no-edit]}}`

- Jump to the previous conflicted parent:

`jj prev --conflict`
