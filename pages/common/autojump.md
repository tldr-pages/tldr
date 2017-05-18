# autojump

> Quickly jump among the directories you visit the most.
> Aliases like j or jc are provided for even less typing.
> TAB key can be used to list the top matches.

- Jump to a directory that contains the given pattern:

`j {{pattern}}`

- Jump to a sub-directory (child) of the current directory that contains the given pattern:

`jc {{pattern}}`

- Run a command (like `ls` or `rm`) with a directory that contains the given pattern as a parameter:

`{{command}} $(j {{pattern}})`

- Remove non-existing directories from the autojump database:

`j --purge`

- Show the entries in the autojump database:

`j -s`
