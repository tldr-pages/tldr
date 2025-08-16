# rexec

> Execute a command on a remote host.
> Note: Use `rexec` with caution, as it transmits data in plain text. Consider secure alternatives like SSH for encrypted communication.
> More information: <https://www.gnu.org/software/inetutils/manual/inetutils.html#rexec-invocation>.

- Execute a command on a remote host:

`rexec {{[-h|--host]}} {{remote_host}} {{ls -l}}`

- Specify the remote username on a remote host:

`rexec {{[-u|--username]}} {{username}} {{[-h|--host]}} {{remote_host}} {{ps aux}}`

- Redirect `stdin` from `/dev/null` on a remote host:

`rexec {{[-n|--noerr]}} {{[-h|--host]}} {{remote_host}} {{ls -l}}`

- Specify the remote port on a remote host:

`rexec {{[-P|--port]}} {{1234}} {{[-h|--host]}} {{remote_host}} {{ls -l}}`
