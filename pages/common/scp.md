# scp

> Secure copy.
> Copy files between hosts using Secure Copy Protocol over SSH.

- Copy a local file to a remote host:

`scp {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}`

- Copy a file from a remote host to a local folder:

`scp {{remote_host}}:{{path/to/remote_file}} {{path/to/local_dir}}`

- Recursively copy the contents of a directory from a remote host to a local directory:

`scp -r {{remote_host}}:{{path/to/remote_dir}} {{path/to/local_dir}}`

- Copy a file between two remote hosts transferring through the local host:

`scp -3 {{host1}}:{{path/to/remote_file}} {{host2}}:{{path/to/remote_dir}}`

- Use a specific username when connecting to the remote host:

`scp {{path/to/local_file}} {{remote_username}}@{{remote_host}}:{{path/to/remote_dir}}`

- Use a specific ssh private key for authentication with the remote host:

`scp -i {{~/.ssh/private_key}} {{local_file}} {{remote_host}}:{{/path/remote_file}}`
