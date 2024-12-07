# eclean

> Clean repository source files and binary packages.
> More information: <https://wiki.gentoo.org/wiki/Eclean>.

- Clean the source file directory:

`sudo eclean distfiles`

- Clean the binary package directory:

`sudo eclean packages`

- Clean the distfiles of all uninstalled packages, but keep the distfiles of installed packages:

`sudo eclean --deep --package-names distfiles`

- Clean the binary packages of all uninstalled packages, but keep the binaries of installed packages:

`sudo eclean --deep --package-names packages`
