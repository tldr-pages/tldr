# git diff

> Show difference in the current file recursivly, no commit ID needed

`git log -p [--follow] [-1] <path>`

> What files are changend accros two branches

`git diff --name-status master..{{name of branch}}`
> Show changes to tracked files.

- Show changes to tracked files:

`git diff {{PATHSPEC}}`

- Show only names of changed files:

`git diff --name-only {{PATHSPEC}}`

- Output a condensed summary of extended header information:

`git diff --summary {{PATHSPEC}}`

- Show staged (added, but not yet committed) changes only:

`git diff --staged`

- Create a patch file:

`git diff > {{target_file.patch}}`
