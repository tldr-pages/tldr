# tlmgr restore

> Restore package backups created with `tlmgr backup`.
> The default backup directory is specified by the `backupdir` option, and can be obtained with `tlmgr option`.
> More information: <https://www.tug.org/texlive/tlmgr.html>.

- List all available backup revisions for all packages:

`tlmgr restore`

- List all available backup revisions for a specific package:

`tlmgr restore {{package}}`

- Restore a specific revision of a specific package:

`tlmgr restore {{package}} {{revision}}`

- Restore the latest revision of all backed-up packages:

`tlmgr restore --all`

- Restore a package from a custom backup directory:

`tlmgr restore {{package}} {{revision}} --backupdir {{path/to/backup_directory}}`

- Perform a dry-run and print all taken actions without making them:

`tlmgr restore --dry-run {{package}} {{revision}}`
