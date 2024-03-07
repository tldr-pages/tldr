# bpkg

> A package manager for Bash scripts.
> More information: <https://github.com/bpkg/bpkg>.

- Update the local index:

`bpkg update`

- Install a package [g]lobally:

`bpkg install --global {{package_name}}`

- Install a package in a subdirectory of the current directory:

`bpkg install {{package_name}}`

- Install a specific version of a package:

`bpkg install {{package_name}}@{{version}} -g`

- Show details about a specific package:

`bpkg show {{package_name}}`

- Run a command, optionally specifying its arguments:

`bpkg run {{command}} {{command_arg1 command_arg2 ...}}`
