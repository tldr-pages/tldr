# yay

> Yet Another Yogurt: A utility for Arch Linux to build and install packages from the Arch User Repository.
> Also see `pacman`.
> More information: <https://github.com/Jguer/yay>.

- Interactively search and install packages from the repos and AUR:

`yay {{package_name|search_term}}`

- Synchronize and update all packages from the repos and AUR:

`yay`

- Synchronize and update only AUR packages:

`yay -Sua`

- Install a new package from the repos and AUR:

`yay -S {{package_name}}`

- Remove an installed package and both its dependencies and configuration files:

`yay -Rns {{package_name}}`

- Search the package database for a keyword from the repos and AUR:

`yay -Ss {{keyword}}`

- Remove orphaned packages (installed as dependencies but not required by any package):

`yay -Yc`

- Show statistics for installed packages and system health:

`yay -Ps`
