# dpkg-deb

> Pack, unpack and provide information about Debian archives.
> More information: <https://manpages.debian.org/latest/dpkg/dpkg-deb.html>.

- Display information about a package:

`dpkg-deb --info {{path/to/file.deb}}`

- Display the package's name and version on one line:

`dpkg-deb --show {{path/to/file.deb}}`

- List the package's contents:

`dpkg-deb --contents {{path/to/file.deb}}`

- Extract package's contents into a directory:

`dpkg-deb --extract {{path/to/file.deb}} {{path/to/directory}}`

- Create a package from a specified directory:

`dpkg-deb --build {{path/to/directory}}`
