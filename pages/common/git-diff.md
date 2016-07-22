# git diff

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
