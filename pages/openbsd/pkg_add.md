# pkg_add

> Install/update packages in OpenBSD.
> See also: `pkg_info`, `pkg_delete`.
> More information: <https://man.openbsd.org/pkg_add>.

- Update all packages, including dependencies:

`pkg_add -u`

- Install a new package:

`pkg_add {{package}}`

- Install packages from the raw output of `pkg_info`:

`pkg_add -l {{path/to/file}}`
