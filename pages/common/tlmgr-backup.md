# tlmgr backup

> Manage backups of TeX Live packages.
> The default backup location is saved in the `backupdir` setting, which can be optained with `tlmgr option`.
> More information: <https://www.tug.org/texlive/tlmgr.html>.

- Make a backup of one or more packages:

`tlmgr backup {{package1 package2 ...}}`

- Make a backup of all packages:

`tlmgr backup --all`

- Make a backup to a specific directory:

`tlmgr backup {{package}} --backupdir {{path/to/backup_directory}}`

- Remove a backup of one or more packages:

`tlmgr backup clean {{package1 package2 ...}}`

- Remove all backups:

`tlmgr backup clean --all`
