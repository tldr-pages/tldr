# sftp

> Secure file transfer program.
> Copy files between hosts using Secure File Transfer Protocol over SSH.

- Connect to a remote server and enter an interactive command mode:

`sftp {{remote_user}}@{{remote_host}}`

- Connect using an alternate port:

`sftp -P {{remote_port}} {{remote_host}}`

- Copy a local file to a remote host:

`sftp {{local_file}} {{remote_host}}:{{/path/remote_file}}`

- Copy a remote file to the local host:

`sftp {{remote_host}}:{{/path/remote_file}} {{local_file}}`
