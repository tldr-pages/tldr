# slapt-get

> An apt like system for Slackware package management.
> Package sources need to be configured on the slapt-getrc file.

- Update the list of available packages and versions (it's recommended to run this before other `slapt-get` commands):

`slapt-get --update`

- Install a package, or update it to the latest available version:

`slapt-get --install {{package}}`

- Remove a package:

`slapt-get --remove {{package}}`

- Upgrade all installed packages to their newest available versions:

`slapt-get --upgrade {{package}}`

- Locate packages of interest by the package name, disk set, or version:

`slapt-get --search {{package}}`

- Show information about packages:

`slapt-get --show {{package}}`
