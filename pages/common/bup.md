# bup

> Very efficient backup system based on the git packfile format.

- Initialize a backup repository in the specified local directory:

`bup -d {{path/to/repository}} init`

- Index folder "my_folder" before of backup:

`bup -d {{path/to/repository}} index {{path/to/my_folder}}`

- Backup a folder to the repository:

`bup -d {{path/to/repository}} save -n {{backup_name}} {{path/to/my_folder}}`

- Show the backup snapshots currently stored in the repository:

`bup -d {{path/to/repository}} ls`

- Restore a specific backup snapshot to a target directory:

`bup -d {{path/to/repository}} restore -C {{path/to/target}} {{backup_name}}`
