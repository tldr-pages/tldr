# emerge

> Gentoo Linux package manager utility.

- Synchronize all packages:

`emerge --sync`

- Update all packages, including dependencies:

`emerge -uDNav @world`

- Resume a failed updated, skipping the failing package:

`emerge --resume --skipfirst`

- Install a new package, with confirmation:

`emerge -av {{package_name}}`

- Remove a package, with confirmation:

`emerge -Cav {{package_name}}`

- Remove orphaned packages (that were installed only as dependencies):

`emerge -avc`

- Search the package database for a keyword:

`emerge -S {{keyword}}`
