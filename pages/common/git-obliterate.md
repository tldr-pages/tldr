# git obliterate

> Delete specific files and erase their history from a Git repository.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-obliterate>.

- Erase the existence of specific files:

`git obliterate {{file_1 file_2 ...}}`

- Erase the existence of specific files between 2 commits:

`git obliterate {{file_1 file_2 ...}} -- {{commit_hash_1}}..{{commit_hash_2}}`
