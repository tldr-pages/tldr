# pacman-mirrors

> Generate a `pacman` mirrorlist for Manjaro Linux.
> Every run of `pacman-mirrors` requires you to synchronize your database and update your system using `sudo pacman -Syyu`.
> See also: `pacman`.
> More information: <https://wiki.manjaro.org/index.php?title=Pacman-mirrors>.

- Generate a mirrorlist using the default settings:

`sudo pacman-mirrors --fasttrack`

- Get the status of the current mirrors:

`pacman-mirrors --status`

- Display the current branch:

`pacman-mirrors --get-branch`

- Switch to a different branch:

`sudo pacman-mirrors --api --set-branch {{stable|unstable|testing}}`

- List available countries:

`pacman-mirrors --country-list`

- Generate a mirrorlist using only mirrors in specific countries:

`sudo pacman-mirrors --country {{United_States,France,Germany,...}}`
