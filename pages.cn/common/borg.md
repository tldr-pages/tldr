# borg

> Deduplicating backup tool.
> Creates local or remote backups that are mountable as filesystems.

- Initialise a (local) repository:

`borg init {{/path/to/repo_folder}}`

- Backup a folder into the repository, creating an archive called "Monday":

`borg create --progress {{/path/to/repo_folder}}::{{Monday}} {{/path/to/source_folder}}`

- List all archives in a repository:

`borg list {{/path/to/repo_folder}}`

- Extract a specific folder from the "Monday" archive in a remote repository, excluding all *.ext files:

`borg extract {{user}}@{{host}}:{{/path/to/repo_folder}}::{{Monday}} {{path/to/target_folder}} --exclude '{{*.ext}}'`

- Prune a repository by deleting all archives older than 7 days, listing changes:

`borg prune --keep-within {{7d}} --list {{/path/to/repo_folder}}`

- Mount a repository as a FUSE filesystem:

`borg mount {{/path/to/repo_folder}}::{{Monday}} {{/path/to/mountpoint}}`

- Display help on creating archives:

`borg create --help`
