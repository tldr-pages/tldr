# pamac

> Command line utility of the GUI package management pamac.

- Check for package updates:

`pamac checkupdates`

- Install a new package:

`pamac install {{package_name}}`

- Remove a package and its no longer required dependencies (orphans):

`pamac remove -o {{package_name}}`

- Search the package database for a package:

`pamac search {{package_name}}`

- List installed packages:

`pamac list -i`
