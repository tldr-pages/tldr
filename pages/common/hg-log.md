# hg log

> Display the revision history of the repository.
> More information: <https://www.mercurial-scm.org/doc/hg.1.html#log>.

- Display the entire revision history of the repository:

`hg log`

- Display the revision history with an ASCII graph:

`hg log --graph`

- Display the revision history with file names matching a specified pattern:

`hg log --include {{pattern}}`

- Display the revision history, excluding file names that match a specified pattern:

`hg log --exclude {{pattern}}`

- Display the log information for a specific revision:

`hg log --rev {{revision}}`

- Display the revision history for a specific branch:

`hg log --branch {{branch}}`

- Display the revision history for a specific date:

`hg log --date {{date}}`

- Display revisions committed by a specific user:

`hg log --user {{user}}`
