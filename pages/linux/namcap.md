# namcap

> Check binary packages and source `PKGBUILD`s for common packaging mistakes.
> More information: <https://wiki.archlinux.org/title/Namcap>.

- To run `namcap` on `PKGBUILD` file:

`namcap PKGBUILD`

- To run `namcap` on file `pkg.tar.xz`:

`namcap pkg.tar.xz`

- Check a file printing extra [i]nformational messages:

`nnamcap -i {{path/to/file}}`
