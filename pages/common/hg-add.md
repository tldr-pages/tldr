# hg add

> Adds specified files to the staging area for the next commit in Mercurial.
> See the `hg` page for additional information.

- Add files or directories to the staging area:

`hg add {{path/to/file}}`

- Add all unstaged files matching a specified pattern:

`hg add --include {{pattern}}`

- Add all unstaged files excluding those that match a specified pattern:

`hg add --exclude {{pattern}}`

- Recurse into sub-repositories:

`hg add --subrepos`

- Test-run without performing any actions:

`hg add --dry-run`
