# sftp

> Secure File Transfer Program.
> Interactive program to copy files between hosts over SSH.
> For non-interactive file transfers, see `scp` or `rsync`.

- Connect to a remote server and enter an interactive command mode:

`sftp {{remote_user}}@{{remote_host}}`

- Connect using an alternate port:

`sftp -P {{remote_port}} {{remote_user}}@{{remote_host}}`

- Transfer remote file to the local system:

`get {{/path/remote_file}}`

- Transfer local file to the remote system:

`put {{/path/local_file}}`

- Transfer remote folder to the local system recursively (works with `put` too):

`get -R {{/path/remote_folder}}`

- Get list of files on local machine:

`lls`

- Get list of files on remote machine:

`ls`
