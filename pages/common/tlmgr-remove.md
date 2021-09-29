# tlmgr remove

> Uninstall TeX Live packages.
> By default, removed packages will be backed up to `./tlpkg/backups` under the TL installation directory.
> More information: <https://www.tug.org/texlive/tlmgr.html>.

- Uninstall a TeX Live package:

`sudo tlmgr remove {{package}}`

- Simulate uninstalling a package without making any changes:

`tlmgr remove --dry-run {{package}}`

- Uninstall a package without its dependencies:

`sudo tlmgr remove --no-depends {{package}}`

- Uninstall a package and back it up to a specific directory:

`sudo tlmgr remove --backupdir {{path/to/directory}} {{package}}`

- Uninstall all of TeX Live, asking for confirmation:

`sudo tlmgr remove --all`
