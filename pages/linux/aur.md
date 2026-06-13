# aur

> Build packages from the AUR and manage local repositories.
> Note: A local repository needs to be defined in `/etc/pacman.conf` and `vifm` needs to be installed for this to fully function.
> More information: <https://github.com/aurutils/aurutils>.

- Initialize the repository that matches the path in `/etc/pacman.conf`:

`repo-add {{path/to/database.db.tar.gz}}`

- Search the AUR database for a package:

`aur search {{keyword}}`

- Download one or more packages and their dependencies from the AUR, build them, and add them to a local repository:

`aur sync {{package1 package2 ...}}`

- List packages available in your local repository:

`aur repo {{[-l|--list]}}`

- Upgrade local repository packages:

`aur sync {{[-u|--upgrades]}}`

- Clean build files after install:

`aur sync {{[-C|--clean]}} {{package}}`

- Install a package without viewing changes in Vim and do not confirm dependency installation:

`aur sync --noview {{[-n|--noconfirm]}} {{package}}`

- Remove a package form the repository metadata (does not remove the package file itself):

`repo-remove {{path/to/database.db.tar.gz}} {{package}}`
