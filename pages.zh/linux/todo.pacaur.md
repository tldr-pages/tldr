# pacaur

> A utility for Arch Linux to build and install packages from the Arch User Repository.

- Synchronize and update all packages (includes AUR):

`pacaur -Syu`

- Synchronize and update only AUR packages:

`pacaur -Syua`

- Install a new package (includes AUR):

`pacaur -S {{package_name}}`

- Remove a package and its dependencies (includes AUR packages):

`pacaur -Rs {{package_name}}`

- Search the package database for a keyword (includes AUR):

`pacaur -Ss {{keyword}}`

- List all currently installed packages (includes AUR packages):

`pacaur -Qs`
