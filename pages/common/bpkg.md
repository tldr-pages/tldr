# bpkg

> A package manager for Bash scripts.
> More information: <https://github.com/bpkg/bpkg>.

- Update the local index:

`bpkg update`

- Install a package globally:

`bpkg install --global {{package}}`

- Install a package in a subdirectory of the current directory:

`bpkg install {{package}}`

- Install a specific version of a package globally:

`bpkg install {{package}}@{{version}} -g`

- Show details about a specific package:

`bpkg show {{package}}`

- Run a command, optionally specifying its arguments:

`bpkg run {{command}} {{argument1 argument2 ...}}`
