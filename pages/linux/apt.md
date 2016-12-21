# apt

> Debian and Ubuntu package management utility.

- Synchronize list of packages and versions available. This should be run first, before running subsequent apt commands:

`apt update`

- Install a new package:

`apt install {{package}}`

- Remove a package:

`apt remove {{package}}`

- Upgrade installed packages to newest available versions:

`apt upgrade`

- Remove no longer needed packages:

`apt autoremove`

- Upgrade installed packages (like "upgrade"), but remove obsolete packages and install additional packages to meet new dependencies:

`apt dist-upgrade`
