# git squash

> Squash N last changes up to a ref'ed commit.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-squash>.

- Squash everything from a specific branch info the current branch:

`git squash {{source-branch|commit-ref}}`

- Squash the `n` latest commits and commit with a message:

`git squash HEAD~{{n}} "{{message}}"`

- Squash the `n` latest commits and commit concatenating all messages:

`git squash --squash-msg @~{{n}}`
