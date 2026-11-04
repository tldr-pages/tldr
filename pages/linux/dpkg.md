# dpkg

> Debian package manager.
> For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Some subcommands such as `deb` have their own usage documentation.
> More information: <https://manned.org/dpkg>.

- Install a package:

`sudo dpkg {{[-i|--install]}} {{path/to/file.deb}}`

- Remove a package:

`sudo dpkg {{[-r|--remove]}} {{package}}`

- List installed packages:

`dpkg {{[-l|--list]}} {{pattern}}`

- List a package's contents:

`dpkg {{[-L|--listfiles]}} {{package}}`

- List contents of a local package file:

`dpkg {{[-c|--contents]}} {{path/to/file.deb}}`

- Find out which package owns a file:

`dpkg {{[-S|--search]}} {{path/to/file}}`

- Purge an installed or already removed package, including configuration:

`sudo dpkg {{[-P|--purge]}} {{package}}`
