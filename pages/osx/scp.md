# scp

> Copies files between hosts on a network
> Works over a secure connection (SSH)

- upload a file or directory

`scp {{/local/file}} {{10.0.0.1}}:{{/remote/path/}}`
`scp {{/local/file}} {{10.0.0.1}}:{{/remote/path/newname}}`
`scp -r {{/local/folder}} {{10.0.0.1}}:{{/remote/path/}}`

- download a file (reversed)

`scp {{10.0.0.1}}:{{/remote/path/filename}} {{/local/file}}`

- specify credentials

`scp {{/local/file}} {{my_user}}@{{10.0.0.1}}:{{/remote/path/}}`
