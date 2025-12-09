# spi

> A meta package manager that handles both packages and slackbuilds.
> More information: <https://github.com/gapan/spi/blob/master/man/spi.t2t>.

- Update the list of available packages and slackbuilds:

`spi {{[-u|--update]}}`

- Install a package or slackbuild:

`spi {{[-i|--install]}} {{package/slackbuild_name}}`

- Upgrade all installed packages to the latest versions available:

`spi {{[-U|--upgrade]}}`

- Locate packages or slackbuilds by package name or description:

`spi {{search_terms}}`

- Display information about a package or slackbuild:

`spi --show {{package/slackbuild_name}}`

- Purge the local package and slackbuild caches:

`spi --clean`
