# scp

> Secure copy.
> Copy files between hosts using Secure Copy Protocol over SSH.

- Copy a local file to a remote host:

`scp {{local_file}} {{remote_host}}:{{/path/remote_file}}`

- Copy a file from a remote host to a local folder:

`scp {{remote_host}}:{{/path/remote_file}} {{/path/local_dir}}`

- Recursively copy the contents of a directory on a remote host to a local directory:

`scp -r {{/path/local_dir}} {{remote_host}}:{{/path/remote_dir}}`

- Copy a file between two remote hosts transferring through the local host:

`scp -3 {{host1}}:{{/path/remote_file.ext}} {{host2}}:{{/path/remote_dir}}`

- Use a specific username when connecting to the remote host:

`scp {{local_file}} {{remote_username}}@{{remote_host}}:{{/remote/path}}`

- Use a specific ssh private key for authentication with the remote host:

`scp -i {{~/.ssh/id_rsa}} {{local_file}} {{remote_host}}:{{/path/remote_file}}`
