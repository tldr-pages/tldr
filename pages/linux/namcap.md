# namcap

> A tool to check binary packages and source PKGBUILDs for common packaging mistakes, which can also be automatically enabled.
> More information: <https://wiki.archlinux.org/title/Namcap>.

- To run `namcap` on a file, where filename is `PKGBUILD` or the name of a binary pkg.tar.xz:

`namcap {{filename}}`

- To see extra informational messages, invoke `namcap` with the -i flag:

`namcap -i {{filename}}`
