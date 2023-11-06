# rsync

> Transfer files either to or from a remote host (but not between two remote hosts), by default using SSH.
> To specify a remote path, use `host:path/to/file_or_directory`.
> More information: <https://download.samba.org/pub/rsync/rsync.1>.

- Transfer a file:

`rsync {{path/to/source}} {{path/to/destination}}`

- Use archive mode (recursively copy directories, copy symlinks without resolving and preserve permissions, ownership and modification times):

`rsync --archive {{path/to/source}} {{path/to/destination}}`

- Compress the data as it is sent to the destination, display verbose and human-readable progress, and keep partially transferred files if interrupted:

`rsync --compress --verbose --human-readable --partial --progress {{path/to/source}} {{path/to/destination}}`

- Recursively copy directories:

`rsync --recursive {{path/to/source}} {{path/to/destination}}`

- Transfer directory contents, but not the directory itself:

`rsync --recursive {{path/to/source}}/ {{path/to/destination}}`

- Recursively copy directories, use archive mode, resolve symlinks and skip files that are newer on the destination:

`rsync --recursive --archive --update --copy-links {{path/to/source}} {{path/to/destination}}`

- Transfer a directory to a remote host running `rsyncd` and delete files on the destination that do not exist on the source:

`rsync --recursive --delete rsync://{{host}}:{{path/to/source}} {{path/to/destination}}`

- Transfer a file over SSH using a different port than the default (22) and show global progress:

`rsync --rsh 'ssh -p {{port}}' --info=progress2 {{host}}:{{path/to/source}} {{path/to/destination}}`
