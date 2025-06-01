# yay

> Yet Another Yogurt: build and install packages from the Arch User Repository.
> See also: `pacman`.
> More information: <https://github.com/Jguer/yay>.

- Interactively search and install packages from the repos and AUR:

`yay {{package_name|search_term}}`

- Synchronize and update all packages from the repos and AUR:

`yay`

- Install a new package from the repos and AUR and do not ask to confirm transactions:

`yay -S {{package}} --noconfirm`

- Remove an installed package and both its dependencies and configuration files:

`yay -Rns {{package}}`

- Search the package database for a keyword from the repos and AUR:

`yay -Ss {{keyword}}`

- Remove orphaned packages (installed as dependencies but not required by any package):

`yay -Yc`

- Clean `pacman` and `yay` caches (old package versions kept for rollback and downgrade purposes):

`yay -Scc`

- Show statistics for installed packages and system health:

`yay -Ps`
