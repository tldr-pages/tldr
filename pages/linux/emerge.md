# emerge

> Gentoo Linux package manager utility.
> For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> More information: <https://wiki.gentoo.org/wiki/Portage#emerge>.

- Synchronize all packages:

`sudo emerge --sync`

- Update all packages, including dependencies:

`sudo emerge -uDNav @world`

- Resume a failed updated, skipping the failing package:

`sudo emerge --resume --skipfirst`

- Install a new package, with confirmation:

`sudo emerge -av {{package}}`

- Remove a package, with confirmation:

`sudo emerge -Cav {{package}}`

- Remove orphaned packages (that were installed only as dependencies):

`sudo emerge -avc`

- Search the package database for a keyword:

`emerge -S {{keyword}}`
