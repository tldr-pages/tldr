# hg log

> Display the revision history of the repository.
> More information: <https://www.mercurial-scm.org/help/commands/log>.

- Display the entire revision history of the repository:

`hg log`

- Display the revision history with an ASCII graph:

`hg log {{[-G|--graph]}}`

- Display the revision history with file names matching a specified pattern:

`hg log {{[-I|--include]}} {{pattern}}`

- Display the revision history, excluding file names that match a specified pattern:

`hg log {{[-X|--exclude]}} {{pattern}}`

- Display the log information for a specific revision:

`hg log {{[-r|--rev]}} {{revision}}`

- Display the revision history for a specific branch:

`hg log {{[-b|--branch]}} {{branch}}`

- Display the revision history for a specific date:

`hg log {{[-d|--date]}} {{date}}`

- Display revisions committed by a specific user:

`hg log {{[-u|--user]}} {{user}}`
