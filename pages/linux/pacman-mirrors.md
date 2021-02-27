# pacman-mirrors

> Generate pacman mirrorlist for Manjaro Linux
> More information: <https://wiki.manjaro.org/index.php?title=Pacman-mirrors>.

- Generate a mirrorlist, using the default settings:

`sudo pacman-mirrors -f`

- Get the status of the current mirrors:

`sudo pacman-mirrors --status`

- Check, which branch you are on:

`sudo pacman-mirrors --get-branch`

- Switch to a different branch:

`sudo pacman-mirrors --api --setbranch {{stable|unstable|testing}}`

- Generate a mirrorlist, only using mirrors in your country:

`sudo pacman-mirrors --geoip`
