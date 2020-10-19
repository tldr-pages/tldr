# bup

> Backup system based on the git packfile format, providing incremental saves and global deduplication.
> More information: <https://github.com/bup/bup>.

- Initialize a backup repository in the specified local directory:

`bup -d {{path/to/repository}} init`

- Prepare a given directory before taking a backup:

`bup -d {{path/to/repository}} index {{path/to/directory}}`

- Backup a directory to the repository:

`bup -d {{path/to/repository}} save -n {{backup_name}} {{path/to/directory}}`

- Show the backup snapshots currently stored in the repository:

`bup -d {{path/to/repository}} ls`

- Restore a specific backup snapshot to a target directory:

`bup -d {{path/to/repository}} restore -C {{path/to/target_directory}} {{backup_name}}`
