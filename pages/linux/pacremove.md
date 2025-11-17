# pacremove

> Remove alpm packages.
> Convenience wrapper for `pactrans --remove`.
> See also: `pactrans`, `pacinstall`.
> More information: <https://github.com/andrewgregory/pacutils/blob/master/doc/pactrans.pod>.

- Remove a package:

`pacremove {{package}}`

- Remove multiple packages:

`pacremove {{package1 package2 ...}}`

- Perform a dry run showing what would be removed:

`pacremove --print-only {{package}}`

- Remove a package without prompting for confirmation:

`pacremove --no-confirm {{package}}`

- Remove a package and its unneeded dependencies:

`pacremove --recursive {{package}}`

- Remove a package and all packages that depend on it:

`pacremove --cascade {{package}}`

- Display help:

`pacremove --help`
