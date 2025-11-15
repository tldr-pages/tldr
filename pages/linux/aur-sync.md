# aur sync

> Download and build AUR packages automatically.
> Note: A local repository needs to be defined in `/etc/pacman.conf` and `vifm` needs to be installed for this to fully function.
> More information: <https://github.com/aurutils/aurutils>.

- Download one or more packages and their dependencies from the AUR, build them, and add them to a local repository:

`aur sync {{package1 package2 ...}}`

- Upgrade local repository packages:

`aur sync {{[-u|--upgrades]}}`

- Clean build files after install:

`aur sync {{[-C|--clean]}} {{package}}`

- Install a package without viewing changes in Vim and do not confirm dependency installation:

`aur sync --noview {{[-n|--noconfirm]}} {{package}}`

- Ignore specific packages when upgrading:

`aur sync {{[-u|--upgrades]}} --ignore {{package1,package2,...}}`
