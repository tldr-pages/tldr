# pkgin

> Manage `pkgsrc` binary packages on NetBSD.
> More information: <https://pkgin.net/#usage>.

- Install a package:

`pkgin install {{package}}`

- Remove a package and its dependencies:

`pkgin remove {{package}}`

- Upgrade all packages:

`pkgin full-upgrade`

- Search for a package:

`pkgin search {{keyword}}`

- List installed packages:

`pkgin list`

- Remove unneeded dependencies:

`pkgin autoremove`
