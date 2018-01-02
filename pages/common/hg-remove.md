# hg remove

> Remove specified files from the staging area.

- Remove files or directories from the staging area:

`hg remove {{path/to/file}}`

- Remove all staged files matching a specified pattern:

`hg remove --include {{pattern}}`

- Remove all staged files, excluding those that match a specified pattern:

`hg remove --exclude {{pattern}}`

- Recursively remove sub-repositories:

`hg remove --subrepos`

- Record a deletion status for files that have been physically removed, but not from the repository:

`hg remove --after`
