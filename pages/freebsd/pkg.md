# pkg

> FreeBSD package manager.
> More information: <https://man.freebsd.org/cgi/man.cgi?query=pkg&sektion=8>.

- Install a new package:

`pkg install {{package}}`

- Delete a package:

`pkg delete {{package}}`

- Upgrade all packages:

`pkg upgrade`

- Search for a package:

`pkg search {{keyword}}`

- List installed packages:

`pkg info`

- Remove unneeded dependencies:

`pkg autoremove`
