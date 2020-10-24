# hg add

> Adds specified files to the staging area for the next commit in Mercurial.
> More information: <https://www.mercurial-scm.org/doc/hg.1.html#add>.

- Add files or directories to the staging area:

`hg add {{path/to/file}}`

- Add all unstaged files matching a specified pattern:

`hg add --include {{pattern}}`

- Add all unstaged files, excluding those that match a specified pattern:

`hg add --exclude {{pattern}}`

- Recursively add sub-repositories:

`hg add --subrepos`

- Perform a test-run without performing any actions:

`hg add --dry-run`
