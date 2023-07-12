# emerge

> Gentoo Linux package manager utility.
> For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> More information: <https://wiki.gentoo.org/wiki/Portage#emerge>.

- Synchronize all packages:

`emerge --sync`

- Update all packages, including dependencies:

`emerge -uDNav @world`

- Resume a failed updated, skipping the failing package:

`emerge --resume --skipfirst`

- Install a new package, with confirmation:

`emerge -av {{package}}`

- Remove a package, with confirmation:

`emerge -Cav {{package}}`

- Remove orphaned packages (that were installed only as dependencies):

`emerge -avc`

- Search the package database for a keyword:

`emerge -S {{keyword}}`
