# dpkg

> Debian package manager.

- Install a package:

`dpkg -i {{path/to/file.deb}}`

- Remove a package:

`dpkg -r {{package_name}}`

- List installed packages:

`dpkg -l {{pattern}}`

- List package contents:

`dpkg -L {{package_name}}`

- List contents of a local package file:

`dpkg -c {{path/to/file.deb}}`

- Find out which package owns a file:

`dpkg -S {{filename}}`
