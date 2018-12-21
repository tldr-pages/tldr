# restic

> Fast, secure, efficient backup program.

- Initialize a backup repository in the specified local directory:

`restic init -r {{path/to/repository}}`

- Backup folder "my_folder" to the repository:

`restic -r {{path/to/repository}} backup {{path/to/my_folder}}`

- Show backup snapshots currently stored in the repository:

`restic -r {{path/to/repository}} snapshots`

- Restore a specific backup snapshot to a target directory:

`restic -r {{path/to/repository}} restore {{snapshot_id}} {{path/to/target}}`

- Restore a specific path from a specific backup to a target directory:

`restic -r {{path/to/repository}} --include {{path/to/restore}} --target {{path/to/target}} restore {{snapshot_id}}`

- Clean up the repository and keep only the most recent snapshot of each unique backup:

`restic forget --keep-last 1 --prune`
