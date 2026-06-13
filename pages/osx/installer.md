# installer

> Install system software and packages to a specified domain or volume.
> More information: <https://keith.github.io/xcode-man-pages/installer.8.html>.

- Install a Python package to the root volume with verbose output:

`sudo installer -verbose {{[-pkg|-package]}} {{path/to/python-version.pkg}} {{[-tgt|-target]}} /`

- Display list of packages (or subpackages for `.mpkg`) that can be installed on the target volume:

`installer -pkginfo {{[-pkg|-package]}} {{path/to/package.pkg}}`

- Display list of volumes onto which the package can be installed:

`installer -volinfo {{[-pkg|-package]}} {{path/to/package.pkg}}`

- Display list of domains into which the package can be installed:

`installer -dominfo {{[-pkg|-package]}} {{path/to/package.pkg}}`

- Generate XML of install choices for a package:

`installer {{[-pkg|-package]}} {{path/to/package.pkg}} -showChoiceChangesXML`

- Install package using XML config instead of command line parameters:

`sudo installer {{[-pkg|-package]}} {{path/to/package.pkg}} -file {{path/to/config-file}}`
