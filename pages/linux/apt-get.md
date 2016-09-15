# apt-get

> Debian and Ubuntu package management utility.

- Synchronize list of packages and versions available. This should be run first, before running subsequent apt-get commands:

`apt-get update`

- Install a new package:

`apt-get install {{package}}`

- Remove a package:

`apt-get remove {{package}}`

- Upgrade installed packages to newest available versions:

`apt-get upgrade`

- Remove no longer needed packages:

`apt-get autoremove`

- Upgrade installed packages (like "upgrade"), but remove obsolete packages and install additional packages to meet new dependencies:

`apt-get dist-upgrade`
