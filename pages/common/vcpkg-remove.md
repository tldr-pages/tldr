# vcpkg remove

> Uninstall packages installed with `vcpkg`.
> More information: <https://learn.microsoft.com/vcpkg/commands/remove>.

- Remove one or more packages:

`vcpkg remove {{package1 package2 ...}}`

- Remove a package for a specific triplet:

`vcpkg remove {{package}}:{{x64-windows}}`

- Remove all outdated packages:

`vcpkg remove --outdated`
