# git summary

> Display data about a Git repository, gives the following information: repository name, repository age, days active, total amount of commits, total amount of files and committer information.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-summary>.

- Display data about a Git repository (see description for more information):

`git summary`

- Display data about a Git repository since a commit-ish:

`git summary {{commit-ish}}`

- Display data about a Git repository, merging committers using different emails into 1 statistic:

`git summary --dedup-by-email`
