# git squash

> Squash multiple commits into a single commit.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-squash>.

- Squash everything from a specific branch into the current branch:

`git squash {{source-branch}}`

- Squash all commits starting with a specific commit on the current branch:

`git squash {{commit-ref}}`

- Squash the `n` latest commits and commit with a message:

`git squash HEAD~{{n}} "{{message}}"`

- Squash the `n` latest commits and commit concatenating all individual messages:

`git squash --squash-msg HEAD~{{n}}`
