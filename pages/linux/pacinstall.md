# pacinstall

> Install alpm packages from repositories.
> Convenience wrapper for `pactrans --install`.
> See also: `pactrans`, `pacremove`.
> More information: <https://github.com/andrewgregory/pacutils/blob/master/doc/pactrans.pod>.

- Install a package:

`pacinstall {{package}}`

- Install multiple packages:

`pacinstall {{package1 package2 ...}}`

- Install a package from a specific repository:

`pacinstall {{repository}}/{{package}}`

- Perform a dry run showing what would be installed:

`pacinstall --print-only {{package}}`

- Install a package without prompting for confirmation:

`pacinstall --no-confirm {{package}}`

- Mark installed packages as dependencies:

`pacinstall --as-deps {{package}}`

- Display help:

`pacinstall --help`
