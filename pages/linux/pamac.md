# pamac

> A command line utility for the GUI package manager pamac.
> If AUR is not enabled by default, add --aur (or -a) after a command.

- Install a new package:

`pamac install {{package_name}}`

- Remove a package and its no longer required dependencies (orphans):

`pamac remove -o {{package_name}}`

- Search the package database for a package:

`pamac search {{package_name}}`

- List installed packages:

`pamac list -i`

- Check for package updates:

`pamac checkupdates`

- Upgrade all packages:

`pamac upgrade`
