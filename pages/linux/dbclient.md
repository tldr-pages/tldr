# dbclient

> Lightweight Dropbear Secure Shell client.
> More information: <https://manned.org/dbclient.1>.

- Connect to a remote host:

`ssh {{user}}@{{host}}`

- Connect to a remote host on [p]ort 2222:

`ssh {{user}}@{{host}} -p 2222`

- Connect to a remote host with using a specific [i]dentity key in dropbear format:

`ssh -i {{path/to/key}} {{user}}@{{host}}`

- Run a command on the remote host with a [t]ty allocation allowing interaction with the remote command:

`ssh {{user}}@{{host}} -t command arguments`

- Connect and forward [A]gent connections to remote host:

`ssh -A {{user}}@{{host}}`
