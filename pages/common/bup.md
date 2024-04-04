# bup

> Backup system based on the Git packfile format, providing incremental saves and global deduplication.
> More information: <https://github.com/bup/bup>.

- Initialize a backup repository in a given local [d]irectory:

`bup -d {{path/to/repository}} init`

- Prepare a given [d]irectory before taking a backup:

`bup -d {{path/to/repository}} index {{path/to/directory}}`

- Backup a [d]irectory to the repository specifying its [n]ame:

`bup -d {{path/to/repository}} save -n {{backup_name}} {{path/to/directory}}`

- Show the backup snapshots currently stored in the repository:

`bup -d {{path/to/repository}} ls`

- Restore a specific backup snapshot to a target dire[C]tory:

`bup -d {{path/to/repository}} restore -C {{path/to/target_directory}} {{backup_name}}`
