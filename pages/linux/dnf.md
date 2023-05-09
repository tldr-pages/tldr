# dnf

> Package management utility for RHEL, Fedora, and CentOS (replaces yum).
> For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> More information: <https://dnf.readthedocs.io>.

- Upgrade installed packages to the newest available versions:

`sudo dnf upgrade`

- Search packages via keywords:

`dnf search {{keyword1 keyword2 ...}}`

- Display details about a package:

`dnf info {{package}}`

- Install a new package (use `-y` to confirm all prompts automatically):

`sudo dnf install {{package1 package2 ...}}`

- Remove a package:

`sudo dnf remove {{package1 package2 ...}}`

- List installed packages:

`dnf list --installed`

- Find which packages provide a given command:

`dnf provides {{command}}`

- View all past operations:

`dnf history`
