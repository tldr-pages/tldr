# yay

> Yet Another Yogurt: A utility for Arch Linux to build and install packages from the Arch User Repository.

- Interactively search and install packages from the repos and AUR:

`yay {{package_name}}`

- Synchronize and update all packages from the repos and AUR:

`yay -Syu`

- Synchronize and update only AUR packages:

`yay -Sua`

- Install a new package from the repos and AUR:

`yay -S {{package_name}}`

- Remove a package and its dependencies:

`yay -Rs {{package_name}}`

- Search the package database for a keyword from the repos and AUR:

`yay -Ss {{keyword}}`

- List all currently installed packages:

`yay -Qs`

- Show statistics for installed packages and system health:

`yay -P --stats`
