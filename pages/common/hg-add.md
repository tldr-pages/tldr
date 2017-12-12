# hg add

> Adds specified files to the staging area for the next commit in Mercurial.

- Add all files to the index:

`hg add`

- Add all files matching a specified pattern:

`hg add --include {{pattern}}`

- Add all files excluding those that match a specified pattern:

`hg add --exclude {{pattern}}`

- Recurse into sub-repositories:

`hg add --subrepos`

- Test-run without performing any actions:

`hg add --dry-run`
