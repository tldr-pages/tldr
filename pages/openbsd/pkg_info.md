# pkg_info

> View information about packages in OpenBSD.
> See also: `pkg_add`, `pkg_delete`.
> More information: <https://man.openbsd.org/pkg_info>.

- Search for a package using the package name:

`pkg_info -Q {{package}}`

- Output a list of installed packages for use with `pkg_add -l`:

`pkg_info -mz`
