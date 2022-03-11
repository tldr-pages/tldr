# namcap

> Check binary packages and source `PKGBUILD`s for common packaging mistakes.
> More information: <https://man.archlinux.org/man/namcap.1>.

- Check a specific `PKGBUILD` file:

`namcap {{path/to/pkgbuild}}`

- Check a specific package file:

`namcap {{path/to/package.pkg.tar.zst}}`

- Check a file, printing extra [i]nformational messages:

`namcap -i {{path/to/file}}`
