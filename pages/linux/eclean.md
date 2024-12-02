# eclean

> Clean repository source files and binary packages.
> More information: <https://wiki.gentoo.org/wiki/Eclean>.

- Clean source file directory:

`sudo eclean distfiles`

- Clean binary package directory:

`sudo eclean packages`

- Clean distfiles of all uninstalled packages, but keep distfiles of installed packages:

`sudo eclean --deep --package-names distfiles`

- Clean binary packages of all uninstalled packages, but keep binaries of installed packages:

`sudo eclean --deep --package-names packages`
