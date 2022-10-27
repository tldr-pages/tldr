# git merge-base

> Find a common ancestor of two commits.
> More information: <https://git-scm.com/docs/git-merge-base>.

- Output a best common ancestor of two commits:

`git merge-base {{commit_1}} {{commit_2}}`

- Output all best common ancestors of two commits:

`git merge-base --all {{commit_1}} {{commit_2}}`

- Return 0 if the first commit is an ancestor of the second commit, else 1:

`git merge-base --is-ancestor {{commit_1}} {{commit_2}}`
