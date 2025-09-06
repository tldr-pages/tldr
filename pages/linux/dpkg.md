# dpkg

> Debian package manager.
> Some subcommands such as `deb` have their own usage documentation.
> For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> More information: <https://manned.org/dpkg>.

- Install a package:

`dpkg {{[-i|--install]}} {{path/to/file.deb}}`

- Remove a package:

`dpkg {{[-r|--remove]}} {{package}}`

- List installed packages:

`dpkg {{[-l|--list]}} {{pattern}}`

- List a package's contents:

`dpkg {{[-L|--listfiles]}} {{package}}`

- List contents of a local package file:

`dpkg {{[-c|--contents]}} {{path/to/file.deb}}`

- Find out which package owns a file:

`dpkg {{[-S|--search]}} {{path/to/file}}`

- Purge an installed or already removed package, including configuration:

`dpkg {{[-P|--purge]}} {{package}}`
