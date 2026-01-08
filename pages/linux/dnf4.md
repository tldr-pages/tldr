# dnf4

> Package manager for RHEL 8/9 and older Fedora versions (pre-41).
> For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> More information: <https://dnf.readthedocs.io/en/latest/command_ref.html>.

- Upgrade installed packages to the newest available versions:

`sudo dnf4 {{[up|upgrade]}}`

- Search packages via keywords:

`dnf4 {{[se|search]}} {{keyword1 keyword2 ...}}`

- Display details about a package:

`dnf4 {{[if|info]}} {{package}}`

- Install a new package (use `--assumeyes` to confirm all prompts automatically):

`sudo dnf4 {{[in|install]}} {{package1 package2 ...}}`

- Remove a package:

`sudo dnf4 {{[rm|remove]}} {{package1 package2 ...}}`

- List installed packages:

`dnf4 {{[ls|list]}} --installed`

- Find which packages provide a given command:

`dnf4 {{[wp|provides]}} {{command}}`

- View all past operations:

`dnf4 {{[hist|history]}}`
