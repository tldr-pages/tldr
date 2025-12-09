# dpkg-deb

> Pack, unpack and provide information about Debian archives.
> More information: <https://manned.org/dpkg-deb>.

- Display information about a package:

`dpkg-deb {{[-I|--info]}} {{path/to/file.deb}}`

- Display the package's name and version on one line:

`dpkg-deb {{[-W|--show]}} {{path/to/file.deb}}`

- List the package's contents:

`dpkg-deb {{[-c|--contents]}} {{path/to/file.deb}}`

- Extract package's contents into a directory:

`dpkg-deb {{[-x|--extract]}} {{path/to/file.deb}} {{path/to/directory}}`

- Create a package from a specified directory:

`dpkg-deb {{[-b|--build]}} {{path/to/directory}}`
