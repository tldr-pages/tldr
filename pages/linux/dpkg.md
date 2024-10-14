# dpkg

> Debian package manager.
> Some subcommands such as `deb` have their own usage documentation.
> For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> More information: <https://manned.org/dpkg>.

- Install a package:

`dpkg -i {{path/to/file.deb}}`

- Remove a package:

`dpkg -r {{package}}`

- List installed packages:

`dpkg -l {{pattern}}`

- List a package's contents:

`dpkg -L {{package}}`

- List contents of a local package file:

`dpkg -c {{path/to/file.deb}}`

- Find out which package owns a file:

`dpkg -S {{path/to/file}}`

- Purge an installed or already removed package, including configuration:

`dpkg -P {{package}}`
