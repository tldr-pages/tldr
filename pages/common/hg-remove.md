# hg remove

> Remove specified files from the staging area.
> More information: <https://www.mercurial-scm.org/doc/hg.1.html#remove>.

- Remove files or directories from the staging area:

`hg remove {{path/to/file}}`

- Remove all staged files matching a specified pattern:

`hg remove --include {{pattern}}`

- Remove all staged files, excluding those that match a specified pattern:

`hg remove --exclude {{pattern}}`

- Recursively remove sub-repositories:

`hg remove --subrepos`

- Remove files from the repository that have been physically removed:

`hg remove --after`
