# dnf download

> Download RPM packages from the DNF repositories.
> Not default to `dnf` but supported via `dnf-plugins-core`.
> See also: `dnf`.
> More information: <https://dnf-plugins-core.readthedocs.io/en/latest/download.html>.

- Download the latest version of a package to the current directory:

`dnf download {{package}}`

- Download a package to a specific directory (the directory must exist):

`dnf download {{package}} --destdir {{path/to/directory}}`

- Print the URL where the RPM package can be downloaded from:

`dnf download --url {{package}}`
