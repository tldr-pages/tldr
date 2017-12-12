# hg add

> Adds specified files to the staging area for the next commit in Mercurial.

- Add all unstaged files to the index:

`hg add`

- Add all unstaged files matching a specified pattern:

`hg add --include {{pattern}}`

- Add all unstaged files excluding those that match a specified pattern:

`hg add --exclude {{pattern}}`

- Recurse into sub-repositories:

`hg add --subrepos`

- Test-run without performing any actions:

`hg add --dry-run`
