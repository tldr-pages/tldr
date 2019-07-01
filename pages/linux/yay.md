# yay

> Yet Another Yogurt: A utility for Arch Linux to build and install packages from the Arch User Repository.
> Also see `pacman`.

- Interactively search and install packages from the repos and AUR:

`yay {{package_name|search_term}}`

- Synchronize and update all packages from the repos and AUR:

`yay`

- Synchronize and update only AUR packages:

`yay -Sua`

- Install a new package from the repos and AUR:

`yay -S {{package_name}}`

- Search the package database for a keyword from the repos and AUR:

`yay -Ss {{keyword}}`

- Show statistics for installed packages and system health:

`yay -Ps`
