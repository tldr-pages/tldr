# git revert

> Create new commits which reverse the effect of earlier ones.
> More information: <https://git-scm.com/docs/git-revert>.

- Revert the most recent commit:

`git revert {{@}}`

- Revert the 5th last commit:

`git revert HEAD~{{4}}`

- Revert multiple commits:

`git revert {{master~5..master~2}}`

- Don't create new commits, just change the working tree:

`git revert -n {{0c01a9..9a1743}}`
