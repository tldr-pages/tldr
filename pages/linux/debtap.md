# debtap

> Convert Debian packages into Arch Linux packages.
> See also: `pacman-upgrade`.
> More information: <https://github.com/helixarch/debtap>.

- Update debtap database (before the first run):

`sudo debtap --update`

- Convert the specified package:

`debtap {{path/to/package.deb}}`

- Convert the specified package bypassing all questions, except for editing metadata files:

`debtap --quiet {{path/to/package.deb}}`

- Generate a PKGBUILD file:

`debtap --pkgbuild {{path/to/package.deb}}`
