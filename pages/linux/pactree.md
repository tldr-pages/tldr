# pactree

> Package dependency tree viewer for pacman.
> More information: <https://man.archlinux.org/man/pactree.8>.

- Print the dependency tree of a specific package:

`pactree {{package}}`

- Print what packages depend on a specific package:

`pactree --reverse {{package}}`

- Dump dependencies one per line, skipping duplicates:

`pactree --unique {{package}}`

- Include optional dependencies of a specific package and colorize the output:

`pactree --optional --color {{package}}`

- Display help:

`pactree`
