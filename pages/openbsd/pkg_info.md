# pkg_info

> OpenBSD package manager utility.
> Add packages using `pkg_add`, remove packages using `pkg_delete`.
> More information: <https://man.openbsd.org/pkg_info>.

- Search for package using package name:

`pkg_info -Q {{package}}`

- Output list of installed packages for use with `pkg_add -l {{list}}`:

`pkg_info -mz`
