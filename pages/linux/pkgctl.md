# pkgctl

> A tool for managing Arch Linux packages.
> More information: <https://man.archlinux.org/man/pkgctl.1>.

- Build a package in a clean chroot:

`pkgctl build`

- Build a package for a specific architecture:

`pkgctl build --arch {{x86_64|aarch64}}`

- Search for a package in the official repositories:

`pkgctl search {{package_name}}`

- Clone a package repository:

`pkgctl repo clone {{package_name}}`

- Display the current version of a package:

`pkgctl version {{package_name}}`

- Authenticate with the Arch Linux packaging infrastructure:

`pkgctl auth`

- Display help for a subcommand:

`pkgctl {{build|search|repo|auth}} --help`
