# aptitude

> Debian and Ubuntu package management utility.

- Synchronize list of packages and versions available. This should be run first, before running subsequent aptitude commands:

`aptitude update`

- Install a new package and its dependencies:

`aptitude install {{package}}`

- Search for a package:

`aptitude search {{package}}`

- Remove a package and all packages depending on it:

`aptitude remove {{package}}`

- Upgrade installed packages to newest available versions:

`aptitude upgrade`

- Upgrade installed packages (like `aptitude upgrade`) including removing obsolete packages and installing additional packages to meet new package dependencies:

`aptitude full-upgrade`
