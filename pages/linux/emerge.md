# emerge

> Gentoo Linux package manager utility

- synchronize all packages

`emerge --sync`

- update all packages, including dependencies

`emerge -uDNav @world`

- resume a failed updated, skipping the failing package

`emerge --resume --skipfirst`

- install a new package, with confirmation

`emerge -av {{package-name}}`

- remove a package, with confirmation

`emerge -Cav {{package-name}}`

- remove orphaned packages (that were installed only as dependencies)

`emerge -avc`

- search the package database for a keyword

`emerge -S {{keyword}}`
