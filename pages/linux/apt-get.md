# apt-get

> Debian and Ubuntu package management utility.

- Update the list of available packages and versions (it's recommended to run this before other `apt-get` commands):

`apt-get update`

- Install a new package, or update an existing package to its latest available version:

`apt-get install {{package}}`

- Upgrade all installed packages to their newest available versions:

`apt-get upgrade`

- Remove a package:

`apt-get remove {{package}}`

- Remove all packages that are no longer needed:

`apt-get autoremove`

- Upgrade installed packages (like `upgrade`), but remove obsolete packages and install additional packages to meet new dependencies:

`apt-get dist-upgrade`
