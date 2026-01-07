# dnf

> Package management utility for RHEL, Fedora, and CentOS.
> DNF5 is a C++ rewrite of the DNF package manager featuring improved performance and a smaller size.
> For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> More information: <https://dnf5.readthedocs.io/en/latest/commands/index.html>.

- Upgrade installed packages to the newest available versions:

`sudo dnf {{[up|upgrade]}}`

- Search packages via keywords:

`dnf {{[se|search]}} {{keyword1 keyword2 ...}}`

- Display details about a package:

`dnf {{[if|info]}} {{package}}`

- Install new packages (use `--assumeyes` to confirm all prompts automatically):

`sudo dnf {{[in|install]}} {{package1 package2 ...}}`

- Remove packages:

`sudo dnf {{[rm|remove]}} {{package1 package2 ...}}`

- List installed packages:

`dnf {{[ls|list]}} --installed`

- Find which packages provide a given command:

`dnf provides {{command}}`

- Clean cached data:

`sudo dnf clean {{all|dbcache|expire-cache|metadata|packages}}`
