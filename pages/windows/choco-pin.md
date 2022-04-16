# choco pin

> Pin a package at a specific version with Chocolatey.
> Pinned packages are skipped automatically when upgrading.
> More information: <https://docs.chocolatey.org/en-us/choco/commands/pin>.

- Print all pinned packages and their versions:

`choco pin`

- Pin a specified package at its current version:

`choco pin add --name {{package_name}}`

- Pin a package at a specified version:

`choco pin add --name {{package_name}} --version {{package_version}}`

- Remove a pin for a specified package:

`choco pin remove --name {{package_name}}`
