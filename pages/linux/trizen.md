# trizen

> Arch Linux utility for building packages from the Arch User Repository (AUR).

- Synchronize and update all packages (including AUR):

`trizen -Syua`

- Install a new package (includes AUR packages):

`trizen -S {{package}}`

- Remove a package and its dependencies:

`trizen -Rs {{package}}`

- Search the package database for a keyword (including AUR):

`trizen -Ss {{package}}`

- Show information about a package:

`trizen -Si {{package}}`

- List installed packages and versions:

`trizen -Qe`
