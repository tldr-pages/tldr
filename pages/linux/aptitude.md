# aptitude

> Debian and Ubuntu package management utility

- Synchronize list of packages and versions available. This should be run first, before running subsequent aptitude commands.

`aptitude update`

- install a new package

`aptitude install {{package}}`

- search for a package

`aptitude search {{package}}`

- remove a package

`aptitude remove {{package}}`

- Upgrade installed packages to newest available versions

`aptitude upgrade`

- Upgrade installed packages (like `aptitude upgrade`) including removing obsolete packages and installing additional packages to meet new package dependencies.

`aptitude full-upgrade`
