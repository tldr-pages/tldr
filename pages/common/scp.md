# scp

> Copies files between hosts on a network.
> Works over a secure connection (SSH).

- Upload a file, or upload and rename a file:

`scp {{/local/file.txt}} {{10.0.0.1}}:{{/remote/path/}}`
`scp {{/local/file.txt}} {{10.0.0.1}}:{{/remote/path/newname.txt}}`

- Download a file:

`scp {{10.0.0.1}}:{{/remote/path/file.txt}} {{/local/folder}}`

- Upload or download a directory:

`scp -r {{/local/folder}} {{10.0.0.1}}:{{/remote/path/}}`
`scp -r {{10.0.0.1}}:{{/remote/path}} {{/local/folder}}`

- Specify username on host:

`scp {{/local/file.txt}} {{my_user}}@{{10.0.0.1}}:{{/remote/path}}`

- Copy a file from one host to another:

`scp {{10.0.0.1}}:{{/remote/path/file.txt}} {{20.0.0.2}}:{{/other/remote/path}}`

- Download a file with ssh key:

`scp -i {{/local/key}} {{10.0.0.1}}:{{/remote/path/file.txt}} {{/local/folder}}`
