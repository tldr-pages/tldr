# dpkg-deb

> Pack, unpack and provide information about Debian archives.

- Information about a package:

`dpkg-deb --info {{path/to/file.deb}}`

- Show the package's name and version on one line:

`dpkg-deb --show {{path/to/file.deb}}`

- List the package contents:

`dpkg-deb --contents {{path/to/file.deb}}`

- Extract package contents into a directory:

`dpkg-deb --extract {{path/to/file.deb}} {{path/to/directory}}`

- Create a package from the package directory:

`dpkg-deb --build {{path/to/directory}}`
