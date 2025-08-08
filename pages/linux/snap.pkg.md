# snap

> Manage the "snap" self-contained software packages.
> Similar to what `apt` is for `.deb`.
> More information: <https://manned.org/snap>.

- Search for a package:

`snap find {{query}}`

- Install a package:

`snap install {{package}}`

- Update a package:

`snap refresh {{package}}`

- Update a package to another channel (track, risk, or branch):

`snap refresh {{package}} --channel={{channel}}`

- Update all packages:

`snap refresh`

- Display basic information about installed snap software:

`snap list`

- Uninstall a package:

`snap remove {{package}}`

- Check for recent snap changes in the system:

`snap changes`
