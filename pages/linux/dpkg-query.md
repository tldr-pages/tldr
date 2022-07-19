# dpkg-query

> A tool that shows information about installed packages.
> More information: <https://manpages.debian.org/latest/dpkg/dpkg-query.1.html>.

- List all installed packages:

`dpkg-query --list`

- List installed packages matching a pattern:

`dpkg-query --list '{{pattern}}'`

- List all files installed by a package:

`dpkg-query --listfiles {{package_name}}`

- Show information about a package:

`dpkg-query --status {{package_name}}`

- Search for packages that own files corresponding to the given pattern:

`dpkg-query --search {{filename}}`
