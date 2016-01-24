# yaourt

> Arch Linux utility for building packages from the Arch User Repository

- synchronize and update all packages (including AUR)

`yaourt -Syua`

- install a new package (includes AUR)

`yaourt -S package-name`

- remove a package and its dependencies (includes AUR packages)

`yaourt -Rs package-name`

- search the package database for a keyword (including AUR)

`yaourt -Ss package-name`

- list installed packages, versions, and repositories (AUR packages will be listed under the repository name 'local')

`yaourt -Q`
