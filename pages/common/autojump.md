# autojump

> Quickly jump among the directories you visit the most.
> Aliases like `j` or `jc` are provided for even less typing.
> See also: `bashmarks`.
> More information: <https://github.com/wting/autojump>.

- Add the `autojump` aliases to your shell:

`source /usr/share/autojump/autojump.{{bash|fish|zsh}}`

- Jump to a directory that contains the given pattern:

`j {{pattern}}`

- Jump to a sub-directory (child) of the current directory that contains the given pattern:

`jc {{pattern}}`

- Open a directory that contains the given pattern in the operating system file manager:

`jo {{pattern}}`

- Remove non-existing directories from the `autojump` database:

`j --purge`

- Show the entries in the `autojump` database:

`j {{[-s|--stat]}}`
