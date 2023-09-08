# pkg_delete

> OpenBSD package manager utility.
> Add packages using `pkg_add`, search for packages using `pkg_info`.
> More information: <https://man.openbsd.org/pkg_delete>.

- Delete package:

`pkg_delete {{package}}`

- Delete package, including unused dependencies:

`pkg_delete -a {{package}}`

- Dry-run deletion of package:

`pkg_delete -n {{package}}`
