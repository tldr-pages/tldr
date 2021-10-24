# git summary

> Display information about a Git repository.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-summary>.

- Display data about a Git repository:

`git summary`

- Display data about a Git repository since a commit-ish:

`git summary {{commit|branch_name|tag_name}}`

- Display data about a Git repository, merging committers using different emails into 1 statistic for each author:

`git summary --dedup-by-email`

- Display data about a Git repository, showing the number of lines modified by each contributor:

`git summary --line`
