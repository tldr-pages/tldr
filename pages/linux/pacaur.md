# pacaur

> A utility for Arch Linux to build and install packages from the Arch User Repository.
> More information: <https://github.com/rmarquis/pacaur>.

- Synchronize and update all packages (includes AUR):

`pacaur -Syu`

- Synchronize and update only AUR packages:

`pacaur -Syua`

- Install a new package (includes AUR):

`pacaur -S {{package}}`

- Remove a package and its dependencies (includes AUR packages):

`pacaur -Rs {{package}}`

- Search the package database for a keyword (includes AUR):

`pacaur -Ss {{keyword}}`

- List all currently installed packages (includes AUR packages):

`pacaur -Qs`
