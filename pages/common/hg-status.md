# hg status

> Show files that have changed in the working directory.
> More information: <https://www.mercurial-scm.org/help/commands/status>.

- Display the status of changed files:

`hg status`

- Display only modified files:

`hg status {{[-m|--modified]}}`

- Display only added files:

`hg status {{[-a|--added]}}`

- Display only removed files:

`hg status {{[-r|--removed]}}`

- Display only deleted (but tracked) files:

`hg status {{[-d|--deleted]}}`

- Display changes in the working directory compared to a specified changeset:

`hg status --rev {{revision}}`

- Display only files matching a specified glob pattern:

`hg status {{[-I|--include]}} {{pattern}}`

- Display files, excluding those that match a specified glob pattern:

`hg status {{[-X|--exclude]}} {{pattern}}`
