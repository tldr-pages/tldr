# vcpkg-update

> List installed packages that have newer versions available in the vcpkg catalog.
> More information: <https://learn.microsoft.com/en-us/vcpkg/commands/update>.

- Check all installed packages for available upgrades:

`vcpkg update`

- Update against a specific target triplet:

`vcpkg update --triplet {{triplet}}`

- Force classic mode, ignoring any manifest in the current directory:

`vcpkg update --classic`
