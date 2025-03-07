# aur

> Build packages from the AUR and manage local repositories.
> Note: A local repository needs to be defined in `/etc/pacman.conf` and `vifm` needs to be installed for this to fully function.
> More information: <https://github.com/aurutils/aurutils>.

- Search the AUR database for a package:

`aur search {{keyword}}`

- Download a package and its dependencies from AUR, build them and add them to a local repository:

`aur sync {{package}}`

- List packages available in your local repository:

`aur repo {{[-l|--list]}}`

- Upgrade local repository packages:

`aur sync {{[-u|--upgrades]}}`

- Install a package without viewing changes in Vim and do not confirm dependency installation:

`aur sync --noview {{[-n|--noconfirm]}} {{package}}`
