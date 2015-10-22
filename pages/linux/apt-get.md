# apt-get

> Debian and Ubuntu package management utility

- Synchronize list of packages and versions available. This should be run first, before running subsequent apt-get commands.

`apt-get update`

- install a new package

`apt-get install {{package}}`

- remove a package

`apt-get remove {{package}}`

- Upgrade installed packages to newest available versions

`apt-get upgrade`

- Upgrade installed packages (like "upgrade"), but remove obsolete packages and install additional packages to meet new dependencies

`apt-get dist-upgrade`
