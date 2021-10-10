# tlmgr update

> Update TeX Live packages.
> More information: <https://www.tug.org/texlive/tlmgr.html>.

- Update all TeX Live packages:

`sudo tlmgr update --all`

- Update tlmgr itself:

`sudo tlmgr update --self`

- Update a specific package:

`sudo tlmgr update {{package}}`

- Update all except a specific package:

`sudo tlmgr update --all --exclude {{package}}`

- Update all packages, making a backup of the current packages:

`sudo tlmgr update --all --backup`

- Update a specific package without updating its dependencies:

`sudo tlmgr update --no-depends {{package}}`

- Simulate updating all packages without making any changes:

`sudo tlmgr update --all --dry-run`
