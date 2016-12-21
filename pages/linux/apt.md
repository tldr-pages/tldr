# apt

> Package management utility for Debian based distributions.

- Update list of packages and versions available. This should be run before running further apt commands:

`apt update`

- Search for packages:

`apt search {{package}}`

- Install a new package:

`apt install {{package}}`

- Remove a package (using "purge" instead also removes its configuration files):

`apt remove {{package}}`

- Upgrade installed packages to the newest available versions:

`apt upgrade`

- Remove no longer needed packages:

`apt autoremove`

- Upgrade installed packages and remove no longer needed packages:

`apt full-upgrade`
