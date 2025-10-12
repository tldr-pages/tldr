# rdiff-backup

> Local/remote mirror and incremental backup tool.
> More information: <https://rdiff-backup.net/rdiff-backup.1.html>.

- Back up `path/to/source` to `path/to/backup`:

`rdiff-backup backup {{path/to/source}} {{path/to/backup}}`

- List incremental backups in repository (location path, local or remote):

`rdiff-backup list increments {{repository}}`

- Restore from most recent backup:

`rdiff-backup restore {{path/to/backup}} {{path/to/destination}}`

- Restore backed up files as they were 3 days ago:

`rdiff-backup restore --at 3D {{path/to/backup}} {{path/to/destination}}`
