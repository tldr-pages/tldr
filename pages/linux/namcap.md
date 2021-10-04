# namcap

> Check binary packages and source `PKGBUILD`s for common packaging mistakes.
> More information: <https://wiki.archlinux.org/title/Namcap>.

- Check a specific `PKGBUILD` file:

`namcap {{path/to/pkgbuild}}`

- Check a specific package file:

`namcap {{path/to/package.pkg.tar.zst}}`

- Check a file printing extra [i]nformational messages:

`nnamcap -i {{path/to/file}}`
