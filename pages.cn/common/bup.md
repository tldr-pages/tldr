# bup

> Backup system based on the git packfile format, providing fast incremental saves and global deduplication.

- Initialize a backup repository in the specified local directory:

`bup -d {{path/to/repository}} init`

- Prepare a given folder before taking a backup:

`bup -d {{path/to/repository}} index {{path/to/folder}}`

- Backup a folder to the repository:

`bup -d {{path/to/repository}} save -n {{backup_name}} {{path/to/folder}}`

- Show the backup snapshots currently stored in the repository:

`bup -d {{path/to/repository}} ls`

- Restore a specific backup snapshot to a target directory:

`bup -d {{path/to/repository}} restore -C {{path/to/target_directory}} {{backup_name}}`
