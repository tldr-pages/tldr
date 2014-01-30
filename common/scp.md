# scp

> Copies files between hosts on a network
> Works over a secure connection (SSH)

- upload a file

`scp {{/local/file.txt}} {{10.0.0.1}}:{{/remote/path/}}`

- upload a file and change its name

`scp {{/local/file.txt}} {{10.0.0.1}}:{{/remote/path/newname.txt}}`

- upload a directory

`scp -r {{/local/folder}} {{10.0.0.1}}:{{/remote/path/}}`

- download a file

`scp {{10.0.0.1}}:{{/remote/path/file.txt}} {{/local/folder}}`

- download a directory

`scp -r {{10.0.0.1}}:{{/remote/path}} {{/local/folder}}`

- specify username on host

`scp {{/local/file.txt}} {{my_user}}@{{10.0.0.1}}:{{/remote/path}}`

- copy a file from one host to another

`scp {{10.0.0.1}}:{{/remote/path/file.txt}} {{20.0.0.2}}:{{/other/remote/path}}`
