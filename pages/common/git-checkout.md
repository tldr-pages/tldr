# git checkout

> Checkout a branch or paths to the working tree.

- Create and switch to a new branch:

`git checkout -b {{branch_name}}`

- Switch to an existing local branch:

`git checkout {{branch_name}}`

- Switch to an existing remote branch:

`git checkout --track {{remote_name}}/{{branch_name}}`

- Undo unstaged local modification:

`git checkout .`

- Replace a file in the current working directory with the version of it committed in a given branch:

`git checkout {{branch_name}} -- {{file_name}}`
