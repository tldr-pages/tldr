# git obliterate

> Delete a file and erase its history from a Git repository:
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-obliterate>.

- Remove all existence of a file including history:

`git obliterate {{file_1 file_2 ...}}`

- Remove existence of a file between 2 commits:

`git obliterate {{file_1 file_2 ...}} -- {{commit_hash1}}..{{commit_hash2}}`
