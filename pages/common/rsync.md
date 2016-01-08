# rsync

> Transfers a file either to or from a remote host.
> Does not allow transfer between two remote hosts.
> Can transfer single files or files matched by pattern.

- Transfer file from local to remote host:

`rsync {{path_to_file}} {{remote_host_name}}:{{remote_host_location}}`

- Transfer file from remote host to local:

`rsync {{remote_host_name}}:{{remote_file_location}} {{local_file_location}}`

- Transfer all *.js files in current directory to host 'devbox' as user 'mike':

`rsync *.js mike@devbox:~/projects/cakeStore/styles/`

- Transfer a directory and all its children from a remote to local:

`rsync -r mike@devbox:~/projects/cakeStore /Users/mike/devProjects/`

- Transfer only updated files from remote host:

`rsync -ru mike@devbox:~/projects/ ./projects/`

- Transfer file over SSH and show progress:

`rsync -e ssh --progress {{remote_host_name}}:{{remote_file}} {{local_file}}`
