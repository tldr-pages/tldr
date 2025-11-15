# zypper

> SUSE & openSUSE package management utility.
> For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> More information: <https://en.opensuse.org/SDB:Zypper_manual>.

- Synchronize list of packages and versions available:

`sudo zypper {{[ref|refresh]}}`
- Synchronize list of packages and versions available:
  `zypper {{ref|refresh}}`
  `sudo zypper {{ref|refresh}}`

- Install a new package:
  `zypper {{in|install}} {{package}}`
  `sudo zypper {{in|install}} {{package}}`

- Remove a package:
  `zypper {{rm|remove}} {{package}}`
  `sudo zypper {{rm|remove}} {{package}}`

- Upgrade installed packages to the newest available versions:
  `zypper {{up|update}}`
  `sudo zypper {{up|update}}`

- Search for a package via keyword:
  `zypper search {{keyword}}`

- Install a new package:

`sudo zypper {{[in|install]}} {{package}}`

- Remove a package:

`sudo zypper {{[rm|remove]}} {{package}}`

- Upgrade installed packages to the newest available versions:

`sudo zypper {{[up|update]}}`

- Search package via keyword:

`zypper {{[se|search]}} {{keyword}}`

- Show information related to configured repositories:

`zypper {{[lr|repos]}} --sort-by-priority`
