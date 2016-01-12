# yaourt

> Arch Linux utility for building packages from the Arch User Repository (AUR)

- synchronize and update all packages, including AUR packages which will be re-compiled

`yaourt -Syua`

- install a new package (including AUR packages)

`yaourt -S package-name`

- remove a package and its dependencies (including AUR packages)

`yaourt -Rs package-name`

- search the package database for a keyword (including AUR)

`yaourt -Ss package-name`

- list installed packages, versions, and repositories (AUR packages will be listed under the repository name 'local')

`pacman -Q`
