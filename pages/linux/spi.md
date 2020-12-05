# spi

> A meta package manager that handles both packages and slackbuilds.

- Update the list of available packages and slackbuilds:

`spi --update`

- Install a package or slackbuild:

`spi --install {{package/slackbuild_name}}`

- Upgrade all installed packages to their latest available versions:

`spi --upgrade`

- Locate packages or slackbuilds of interest by the package name or description:

`spi {{search_terms}}`

- Show information about a package or slackbuild:

`spi --show {{package/slackbuild_name}}`

- Purge the local package and slackbuild caches:

`spi --clean`
