# zypper

> SUSE & openSUSE package management utility.
> For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> More information: <https://en.opensuse.org/SDB:Zypper_manual>.

- Synchronize list of packages and versions available:

`zypper refresh`

- Install a new package:

`zypper install {{package}}`

- Remove a package:

`zypper remove {{package}}`

- Upgrade installed packages to the newest available versions:

`zypper update`

- Search package via keyword:

`zypper search {{keyword}}`

- Show information related to configured repositories:

`zypper repos --sort-by-priority`
