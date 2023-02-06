# git revert

> Create new commits which reverse the effect of earlier ones.
> More information: <https://git-scm.com/docs/git-revert>.

- Revert the most recent commit:

`git revert {{HEAD}}`

- Revert the 5th last commit:

`git revert HEAD~{{4}}`

- Revert a specific commit:

`git revert {{0c01a9}}`

- Revert multiple commits:

`git revert {{branch_name~5..branch_name~2}}`

- Don't create new commits, just change the working tree:

`git revert -n {{0c01a9..9a1743}}`
