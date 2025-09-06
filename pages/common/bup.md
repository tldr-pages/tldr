# bup

> Backup system based on the Git packfile format, providing incremental saves and global deduplication.
> More information: <https://manned.org/bup>.

- Initialize a backup repository in a given local directory:

`bup {{[-d|--bup-dir]}} {{path/to/repository}} init`

- Prepare a given directory before taking a backup:

`bup {{[-d|--bup-dir]}} {{path/to/repository}} index {{path/to/directory}}`

- Backup a directory to the repository specifying its name:

`bup {{[-d|--bup-dir]}} {{path/to/repository}} save {{[-n|--name]}} {{backup_name}} {{path/to/directory}}`

- Show the backup snapshots currently stored in the repository:

`bup {{[-d|--bup-dir]}} {{path/to/repository}} ls`

- Restore a specific backup snapshot to a target directory:

`bup {{[-d|--bup-dir]}} {{path/to/repository}} restore {{[-C|--outdir]}} {{path/to/target_directory}} {{backup_name}}`
