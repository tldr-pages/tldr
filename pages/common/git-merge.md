# git merge

> Merge branches.
> More information: <https://git-scm.com/docs/git-merge>.

- Merge branches into your current branch:

`git merge {{branch_name1 branch_name2 ...}}`

- Edit the merge message:

`git merge {{[-e|--edit]}} {{branch_name}}`

- Merge a branch and create a merge commit:

`git merge --no-ff {{branch_name}}`

- Copy the state of a branch into the working tree and stage it (Note: Use `git commit` to create the actual commit):

`git merge --squash {{branch_name}}`

- Abort a merge in case of conflicts:

`git merge --abort`

- Merge using a specific strategy:

`git merge {{[-s|--strategy]}} {{strategy}} {{[-X|--strategy-option]}} {{strategy_option}} {{branch_name}}`
