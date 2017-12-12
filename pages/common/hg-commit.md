# hg commit

> Commit all staged or specified files to the repository.

- Commit staged files to the repository:

`hg commit`

- Commit a specific file or directory:

`hg commit {{path/to/file}}`

- Commit with a specific message:

`hg commit --message {{message}}`

- Commit all files matching a specified pattern:

`hg commit --include {{pattern}}`

- Commit all files, excluding those that match a specified pattern:

`hg commit --exclude {{pattern}}`

- Commit using the interactive mode:

`hg commit --interactive`
