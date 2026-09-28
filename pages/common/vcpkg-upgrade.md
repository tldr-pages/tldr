# vcpkg-upgrade

> Rebuild all outdated packages that were installed in classic mode.
> More information: <https://learn.microsoft.com/en-us/vcpkg/commands/upgrade>.

- Show which packages would be upgraded, without actually upgrading them:

`vcpkg upgrade`

- Actually upgrade all outdated packages:

`vcpkg upgrade --no-dry-run`

- Upgrade outdated packages for a specific target triplet:

`vcpkg upgrade --triplet {{triplet}} --no-dry-run`

- Stop upgrading as soon as a package fails to build, instead of continuing:

`vcpkg upgrade --no-dry-run --no-keep-going`

- Continue with a warning when a port is unsupported, rather than failing:

`vcpkg upgrade --no-dry-run --allow-unsupported`
