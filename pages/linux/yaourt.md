# yaourt

> Arch Linux utility for building packages from the Arch User Repository.
> More information: <https://archlinux.fr/yaourt-en>.

- Synchronize and update all packages (including AUR):

`yaourt -Syua`

- Install a new package (includes AUR):

`yaourt -S {{package}}`

- Remove a package and its dependencies (includes AUR packages):

`yaourt -Rs {{package}}`

- Search the package database for a keyword (including AUR):

`yaourt -Ss {{query}}`

- List installed packages, versions, and repositories (AUR packages will be listed under the repository name `local`):

`yaourt -Q`
