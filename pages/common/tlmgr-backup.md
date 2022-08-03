# tlmgr backup

> Manage backups of TeX Live packages.
> The default backup directory is specified by the `backupdir` option, and can be obtained with `tlmgr option`.
> More information: <https://www.tug.org/texlive/tlmgr.html>.

- Make a backup of one or more packages:

`tlmgr backup {{package1 package2 ...}}`

- Make a backup of all packages:

`tlmgr backup --all`

- Make a backup to a custom directory:

`tlmgr backup {{package}} --backupdir {{path/to/backup_directory}}`

- Remove a backup of one or more packages:

`tlmgr backup clean {{package1 package2 ...}}`

- Remove all backups:

`tlmgr backup clean --all`
