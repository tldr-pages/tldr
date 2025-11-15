# hg add

> Adds specified files to the staging area for the next commit in Mercurial.
> More information: <https://www.mercurial-scm.org/help/commands/add>.

- Add files or directories to the staging area:

`hg add {{path/to/file}}`

- Add all unstaged files matching a specified pattern:

`hg add {{[-I|--include]}} {{pattern}}`

- Add all unstaged files, excluding those that match a specified pattern:

`hg add {{[-X|--exclude]}} {{pattern}}`

- Recursively add sub-repositories:

`hg add {{[-S|--subrepos]}}`

- Perform a test-run without performing any actions:

`hg add {{[-n|--dry-run]}}`
