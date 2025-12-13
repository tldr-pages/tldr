# pkgdiff

> Compare the contents of two Slackware packages.
> See also: `installpkg`, `removepkg`, `upgradepkg`, `makepkg`, `pkgtool`.
> More information: <https://www.slackbook.org/html/package-management-package-utilities.html>.

- Compare two packages and display differences:

`pkgdiff {{path/to/package1.tgz}} {{path/to/package2.tgz}}`

- Compare an installed package with a package file:

`pkgdiff {{installed_package_name}} {{path/to/package.tgz}}`
