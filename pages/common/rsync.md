# rsync

> Transfer files either to or from a remote host (not between two remote hosts).
> Can transfer single files, or multiple files matching a pattern.

- Transfer file from local to remote host:

`rsync {{path/to/local_file}} {{remote_host}}:{{path/to/remote_directory}}`

- Transfer file from remote host to local:

`rsync {{remote_host}}:{{path/to/remote_file}} {{path/to/local_directory}}`

- Transfer file in archive (to preserve attributes) and compressed (zipped) mode with verbose and human-readable progress:

`rsync -azvhP {{path/to/local_file}} {{remote_host}}:{{path/to/remote_directory}}`

- Transfer a directory and all its children from a remote to local:

`rsync -r {{remote_host}}:{{path/to/remote_directory}} {{path/to/local_directory}}`

- Transfer directory contents (but not the directory itself) from a remote to local:

`rsync -r {{remote_host}}:{{path/to/remote_directory}}/ {{path/to/local_directory}}`

- Transfer only updated files from remote host:

`rsync -ru {{remote_host}}:{{path/to/remote_directory}} {{path/to/local_directory}}`

- Transfer file over SSH and delete local files that do not exist on remote host:

`rsync -e ssh --delete {{remote_host}}:{{path/to/remote_file}} {{path/to/local_file}}`

- Transfer file over SSH and show global progress:

`rsync -e ssh --info=progress2 {{remote_host}}:{{path/to/remote_file}} {{path/to/local_file}}`
