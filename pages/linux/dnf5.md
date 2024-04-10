# dnf5

> Package management utility for RHEL, Fedora, and CentOS (it replaces dnf, which in turn replaced yum).
> DNF5 is a complete rewrite of the DNF package manager, written in C++ for improved performance and a smaller size.
> For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> More information: <https://dnf5.readthedocs.io/>.

- Upgrade installed packages to the newest available versions:

`sudo dnf5 upgrade`

- Search packages via keywords:

`dnf5 search {{keyword1 keyword2 ...}}`

- Display details about a package:

`dnf5 info {{package}}`

- Install a new package (Note: use `-y` to confirm all prompts automatically):

`sudo dnf5 install {{package1 package2 ...}}`

- Remove a package:

`sudo dnf5 remove {{package1 package2 ...}}`

- List installed packages:

`dnf5 list --installed`

- Find which packages provide a given command:

`dnf5 provides {{command}}`

- Remove or expire cached data:

`sudo dnf clean all`
