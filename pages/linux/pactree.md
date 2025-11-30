# pactree

> Package dependency tree viewer for pacman.
> More information: <https://manned.org/pactree>.

- Print the dependency tree of a specific package:

`pactree {{package}}`

- Print what packages depend on a specific package:

`pactree {{[-r|--reverse]}} {{package}}`

- Dump dependencies one per line, skipping duplicates:

`pactree {{[-u|--unique]}} {{package}}`

- Include optional dependencies of a specific package and colorize the output:

`pactree {{[-co|--color --optional]}} {{package}}`

- Display help:

`pactree`
