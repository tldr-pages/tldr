# rsync

> Transfer files either to or from a remote host (not between two remote hosts).
> Can transfer single files, or multiple files matching a pattern.

- Transfer file from local to remote host:

`rsync {{path/to/local_file}} {{remote_host}}:{{path/to/remote_directory}}`

- Transfer file from remote host to local:

`rsync {{remote_host}}:{{path/to/remote_file}} {{path/to/local_directory}}`

- Transfer file in [a]rchive (to preserve attributes) and compressed ([z]ipped) mode with [v]erbose and [h]uman-readable [p]rogress:

`rsync -azvhP {{path/to/local_file}} {{remote_host}}:{{path/to/remote_directory}}`

- Transfer a directory and all its children from a remote to local:

`rsync -r {{remote_host}}:{{path/to/remote_directory}} {{path/to/local_directory}}`

- Transfer directory contents (but not the directory itself) from a remote to local:

`rsync -r {{remote_host}}:{{path/to/remote_directory}}/ {{path/to/local_directory}}`

- Transfer a directory [r]ecursively, in [a]rchive to preserve attributes, resolving contained soft[l]inks , and ignoring already transferred files [u]nless newer:

`rsync -rauL {{remote_host}}:{{path/to/remote_file}} {{path/to/local_directory}}`

- Transfer file over SSH and delete local files that do not exist on remote host:

`rsync -e ssh --delete {{remote_host}}:{{path/to/remote_file}} {{path/to/local_file}}`

- Transfer file over SSH and show global progress:

`rsync -e ssh --info=progress2 {{remote_host}}:{{path/to/remote_file}} {{path/to/local_file}}`
