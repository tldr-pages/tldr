# yaourt

> Arch Linux utility for building packages from the Arch User Repository.

- Synchronize and update all packages (including AUR):

`yaourt -Syua`

- Install a new package (includes AUR):

`yaourt -S {{package_name}}`

- Remove a package and its dependencies (includes AUR packages):

`yaourt -Rs {{package_name}}`

- Search the package database for a keyword (including AUR):

`yaourt -Ss {{package_name}}`

- List installed packages, versions, and repositories (AUR packages will be listed under the repository name 'local'):

`yaourt -Q`
