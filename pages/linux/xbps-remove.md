# xbps-remove

> XBPS utility to remove packages.
> See also: `xbps`.
> More information: <https://manned.org/xbps-remove.1>.

- Remove a package:

`xbps-remove {{package}}`

- Remove a package and its dependencies:

`xbps-remove {{[-R|--recursive]}} {{package}}`

- Remove orphan packages (installed as dependencies but no longer required by any package):

`xbps-remove {{[-o|--remove-orphans]}}`

- Remove obsolete packages from the cache:

`xbps-remove {{[-O|--clean-cache]}}`
