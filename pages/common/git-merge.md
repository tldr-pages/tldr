# git merge

> Merge branches.
> More information: <https://git-scm.com/docs/git-merge>.

- Merge a branch into your current branch:

`git merge {{branch_name}}`

- Edit the merge message:

`git merge --edit {{branch_name}}`

- Merge a branch and create a merge commit:

`git merge --no-ff {{branch_name}}`

- Abort a merge in case of conflicts:

`git merge --abort`

- Merge using a specific strategy:

`git merge --strategy {{strategy}} --strategy-option {{strategy_option}} {{branch_name}}`
