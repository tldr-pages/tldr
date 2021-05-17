# git create-branch

> Create a Git branch in a repository.
> Part of `git-extras`
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-create-branch>.

- Create a local branch:

`git create-branch {{branch_name}}`

- Create a branch locally and on origin:

`git create-branch -r {{branch_name}}`

- Create a branch locally and on upstream (through forks):

`git create-branch -r upstream {{branch_name}}`
