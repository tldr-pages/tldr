# rsync

> Transfer files either to or from a remote host (not between two remote hosts).
> Can transfer single files, or multiple files matching a pattern.

- Transfer file from local to remote host:

`rsync {{path/to/file}} {{remote_host_name}}:{{remote_host_location}}`

- Transfer file from remote host to local:

`rsync {{remote_host_name}}:{{remote_file_location}} {{local_file_location}}`

- Transfer file in archive (to preserve attributes) and compressed (zipped) mode with verbose and human-readable progress:

`rsync -azvhP {{path/to/file}} {{remote_host_name}}:{{remote_host_location}}`

- Transfer a directory and all its children from a remote to local:

`rsync -r {{remote_host_name}}:{{remote_directory_location}} {{local_directory_location}}`

- Transfer directory contents (but not the directory itself) from a remote to local:

`rsync -r {{remote_host_name}}:{{remote_directory_location}}/ {{local_directory_location}}`

- Transfer only updated files from remote host:

`rsync -ru {{remote_host_name}}:{{remote_directory_location}} {{local_directory_location}}`

- Transfer file over SSH and delete local files that do not exist on remote host:

`rsync -e ssh --delete {{remote_host_name}}:{{remote_file}} {{local_file}}`

- Transfer file over SSH and show global progress:

`rsync -e ssh --info=progress2 {{remote_host_name}}:{{remote_file}} {{local_file}}`
