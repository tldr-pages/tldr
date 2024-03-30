# pkg_delete

> Remove packages in OpenBSD.
> See also: `pkg_add`, `pkg_info`.
> More information: <https://man.openbsd.org/pkg_delete>.

- Delete a package:

`pkg_delete {{package}}`

- Delete a package, including its unused dependencies:

`pkg_delete -a {{package}}`

- Dry-run deletion of a package:

`pkg_delete -n {{package}}`
