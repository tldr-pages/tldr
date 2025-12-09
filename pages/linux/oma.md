# oma

> A package management frontend for dpkg-based Linux distributions.
> More information: <https://github.com/AOSC-Dev/oma#usage>.

- Enter the interactive package management interface:

`sudo oma`

- Install a package:

`sudo oma install {{package_name}}`

- Remove a package:

`sudo oma remove {{package_name}}`

- Search for a package:

`oma search {{keyword}}`

- Show detailed information for a package:

`oma show`

- Upgrade all installed packages to their latest versions:

`sudo oma upgrade`

- Update the list of available packages and versions (done automatically before `oma install` and `oma upgrade`):

`sudo oma refresh`

- Display help:

`oma help`
