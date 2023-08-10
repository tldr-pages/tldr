# slapt-get

> An apt like system for Slackware package management.
> Package sources need to be configured in the slapt-getrc file.
> More information: <https://software.jaos.org>.

- Update the list of available packages and versions:

`slapt-get --update`

- Install a package, or update it to the latest available version:

`slapt-get --install {{package}}`

- Remove a package:

`slapt-get --remove {{package}}`

- Upgrade all installed packages to their latest available versions:

`slapt-get --upgrade`

- Locate packages by the package name, disk set, or version:

`slapt-get --search {{query}}`

- Show information about a package:

`slapt-get --show {{package}}`
