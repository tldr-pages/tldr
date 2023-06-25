# xbps-remove

> XBPS utility to remove packages.
> See also: `xbps`.
> More information: <https://man.voidlinux.org/xbps-remove.1>.

- Remove a package:

`xbps-remove {{package}}`

- Remove a package and its dependencies:

`xbps-remove --recursive {{package}}`

- Remove orphan packages (installed as dependencies but no longer required by any package):

`xbps-remove --remove-orphans`

- Remove obsolete packages from the cache:

`xbps-remove --clean-cache`
