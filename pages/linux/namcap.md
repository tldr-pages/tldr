# namcap

> Check binary packages and source `PKGBUILD`s for common packaging mistakes.
> More information: <https://manned.org/namcap>.

- Check a specific `PKGBUILD` file:

`namcap {{path/to/pkgbuild}}`

- Check a specific package file:

`namcap {{path/to/package.pkg.tar.zst}}`

- Check a file, printing extra informational messages:

`namcap {{[-i|--info]}} {{path/to/file}}`
