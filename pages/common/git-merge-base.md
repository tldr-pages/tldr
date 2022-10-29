# git merge-base

> Find a common ancestor of two commits.
> More information: <https://git-scm.com/docs/git-merge-base>.

- Print the best common ancestor of two commits:

`git merge-base {{commit_1}} {{commit_2}}`

- Output all best common ancestors of two commits:

`git merge-base --all {{commit_1}} {{commit_2}}`

- Check if a commit is an ancestor of a specific commit:

`git merge-base --is-ancestor {{ancestor_commit}} {{commit}}`
