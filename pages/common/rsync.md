# rsync

> Transfers a file either to or from a remote host
> Does not allow transfer between two remote hosts
> Can transfer single files or files matched by pattern

- transfer file from local to remote host, filename supports regex.

`rsync {{path/to/file}} {{remote_host_name}}:{{remote_host_location}}`

- transfer file from remote host to local

`rsync {{remote_host_name}}:{{remote_file_location}} {{local_file_location}}`

- transfer file in archive (to preserve attributes) and compressed (zipped) mode

`rsync -az {{path/to/file}} {{remote_host_name}}:{{remote_host_location}}`

- transfer a directory and all its children from a remote to local

`rsync -r {{remote_host_name}}:{{remote_folder_location}} {{local_folder_location}}`

- transfer file over SSH and show progress

`rsync -e ssh --progress {{remote_host_name}}:{{remote_file}} {{local_file}}`
