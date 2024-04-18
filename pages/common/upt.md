# upt

> Unified interface for managing packages across various operating systems, like Windows, many Linux distributions, macOS, FreeBSD and even Haiku.
> It requires the native OS package manager to be installed.
> See also: `flatpak`, `brew`, `scoop`, `apt`, `dnf`.
> More information: <https://github.com/sigoden/upt>.

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
