# bup

> Very efficient backup system based on the git packfile format, providing fast incremental saves and global deduplication

- Initialize a backup repository in the specified local directory:

`restic init -r {{path/to/repository}}`

- Backup folder to the repository:

`bup index {{path/to/backup}} && save -n {{name}} {{path/to/backup}}`

- Get a list of your previous backups

`bup ls`

- Restore a specific backup snapshot to a target directory:

`restic -r {{path/to/repository}} restore {{snapshot_id}} {{path/to/target}}`

- Clean up the repository and keep only the most recent snapshot of each unique backup:

`restic forget --keep-last 1 --prune`
