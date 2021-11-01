# git squash

> Squash N last changes up to a ref'ed commit.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-squash>.

- Squash everything from soruce branch or commit reference into HEAD:

`git squash {{source-branch|commit-ref}}`

- Squash and commit with a given message:

`git squash HEAD~3 "Commit message"`

- Squash and concatenate all messages:

`git squash --squash-msg @~3`
