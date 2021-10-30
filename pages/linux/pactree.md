# pactree

> Package dependency tree viewer for pacman.
> More information: <https://man.archlinux.org/man/community/pacman-contrib/pactree.8.en>.

- View the dependency tree of a package:

`pactree {{package}}`

- View what packages depend on this package:

`pactree --reverse {{package}}`

- List dependencies at the start of the line and only with unique entries:

`pactree --unique {{package}}`

- Include optional dependencies of a package and colorize the output:

`pactree --optional --color {{package}}`

- Show the help page:

`pactree`
