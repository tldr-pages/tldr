# git checkout

> Checkout a branch or paths to the working tree.

- Create and switch to a new branch:

`git checkout -b {{branch_name}}`

- Switch to an existing local branch:

`git checkout {{branch_name}}`

- Switch to an existing remote branch:

`git checkout --track {{remote_name}}/{{branch_name}}`

- Discard all unstaged changes in the current folder (see `git reset` for more undo-like commands):

`git checkout .`

- Discard unstaged changes to a given file:

`git checkout {{file_name}}`

- Replace a file in the current folder with the version of it committed in a given branch:

`git checkout {{branch_name}} -- {{file_name}}`
