# debtap

> Convert .deb packages into Arch Linux packages.
> More information: <https://github.com/helixarch/debtap>

- Update debtap database (before first run)

`sudo debtap -u`

- Convert a package

`debtap {{package.deb}}`

- Convert a package (bypass all questions, not recommended)

`debtap -Q {{package.deb}}`

- Then install with pacman

`sudo pacman -U {{package.pkg.tar.zst}}`

- Generate PKGBUILD file

`debtap -P {{package.deb}}`
