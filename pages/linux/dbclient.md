# dbclient

> Lightweight Dropbear Secure Shell client.
> More information: <https://manned.org/dbclient.1>.

- Connect to a remote host:

`dbclient {{user}}@{{host}}`

- Connect to a remote host on [p]ort 2222:

`dbclient {{user}}@{{host}} -p 2222`

- Connect to a remote host using a specific [i]dentity key in dropbear format:

`dbclient -i {{path/to/key_file}} {{user}}@{{host}}`

- Run a command on the remote host with a [t]ty allocation allowing interaction with the remote command:

`dbclient {{user}}@{{host}} -t {{command}} {{argument1 argument2 ...}}`

- Connect and forward [A]gent connections to remote host:

`dbclient -A {{user}}@{{host}}`
