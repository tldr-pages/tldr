# dnf

> Package management utility for RHEL, Fedora, and CentOS (replaces yum).
> Some subcommands such as `group` and `config-manager` have their own usage documentation.
> For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> More information: <https://dnf.readthedocs.io>.

- Upgrade installed packages to the newest available versions:

`sudo dnf {{[up|upgrade]}}`

- Search packages via keywords:

`dnf {{[se|search]}} {{keyword1 keyword2 ...}}`

- Display details about a package:

`dnf {{[if|info]}} {{package}}`

- Install a new package (use `--assumeyes` to confirm all prompts automatically):

`sudo dnf {{[in|install]}} {{package1 package2 ...}}`

- Remove a package:

`sudo dnf {{[rm|remove]}} {{package1 package2 ...}}`

- List installed packages:

`dnf {{[ls|list]}} --installed`

- Find which packages provide a given command:

`dnf {{[wp|provides]}} {{command}}`

- View all past operations:

`dnf {{[hist|history]}}`
