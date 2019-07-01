# git checkout

> Checkout a branch or paths to the working tree.
> More information: <https://git-scm.com/docs/git-checkout>.

- Create and switch to a new branch:

`git checkout -b {{branch_name}}`

- Create and switch to a new branch based on a specific reference (branch, remote/branch, tag are examples of valid references):

`git checkout -b {{branch_name}} {{reference}}`

- Switch to an existing local branch:

`git checkout {{branch_name}}`

- Switch to an existing remote branch:

`git checkout --track {{remote_name}}/{{branch_name}}`

- Discard all unstaged changes in the current directory (see `git reset` for more undo-like commands):

`git checkout .`

- Discard unstaged changes to a given file:

`git checkout {{file_name}}`

- Replace a file in the current directory with the version of it committed in a given branch:

`git checkout {{branch_name}} -- {{file_name}}`
