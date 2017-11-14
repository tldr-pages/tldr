# borg

> Deduplicating backup tool with compression and encryption.
> Supports local and remote backups that are mountable as filesystems.

- Initialise a (local) repository:

`borg init {{/path/to/repo/folder}}`

- Backup a folder into the repository, creating an archive called Monday:

`borg create --progress {{/path/to/repo/folder}}::{{Monday}} {{/path/to/source/folder}}`

- List all archives in a repository:

`borg list {{/path/to/repo/folder}}`

- Extract a specific folder from the 'Monday' archive, excluding all *.ext files:

`borg extract {{/path/to/repo/folder}}::{{Monday}} {{path/to/target/folder}} --exclude '{{*.ext}}'`

- Prune a repository by deleting all archives older than 7 days, listing changes:

`borg prune --keep-within 7d --list {{/path/to/repo/folder}}`

- Mount a repository as a FUSE filesystem:

`borg mount {{/path/to/repo/folder}}::{{Monday}} {{/path/to/mountpoint}}`

- Display help on creating archives:

`borg create --help`
