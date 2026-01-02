# dpkg-query

> Display information about installed packages.
> More information: <https://manned.org/dpkg-query>.

- List all installed packages:

`dpkg-query {{[-l|--list]}}`

- List installed packages matching a pattern:

`dpkg-query {{[-l|--list]}} '{{libc6*}}'`

- List all files installed by a package:

`dpkg-query {{[-L|--listfiles]}} {{libc6}}`

- Show information about a package:

`dpkg-query {{[-s|--status]}} {{libc6}}`

- Search for packages that own files matching a pattern:

`dpkg-query {{[-S|--search]}} {{/etc/ld.so.conf.d}}`
