# upt

> Unified interface for managing packages across various operating systems.
> It requires the OS package manager to be installed.
> See also: `flatpak`, `apt`, `dnf`, `yum`.
> More information: [Upt Documentation](upt-docs.com).

- Update the list of available packages:

`upt update`

- Search for a given package:

`upt search {{search_term}}`

- Show information for a package:

`upt info {{package}}`

- Install a given package:

`upt install {{package}}`

- Remove a given package:

`upt {{remove|uninstall}} {{package}}`

- Upgrade all installed packages:

`upt upgrade`

- Upgrade a given package:

`upt upgrade {{package}}`

- List installed packages:

`upt list`
