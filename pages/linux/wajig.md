# wajig

> Wajig is a simplified, all-in-one-place, system support tool for Debian and Ubuntu.
> More information: <https://wajig.togaware.com/>

- Update the list of available packages and versions:

`wajig update`

- Install a package, or update it to the latest available version:

`wajig install {{package}}`

- Remove a package:

`wajig remove {{package}}`

- Remove a package and its configuration files:

`wajig purge {{package}}`

- Upgrade all installed packages to their newest available versions:

`wajig upgrade`

- Perform an update then a dist-upgrade:

`wajig daily-upgrade`

- Display installed sizes of given packages:

`wajig sizes`

- List version and distribution of given packages:

`wajig versions`

- List versions of upgradable packages:

`wajig toupgrade`

- Display packages which have some form of dependency on the given package:

`wajig dependents`
