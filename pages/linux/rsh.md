# rsh

> Execute commands on a remote host.
> More information: <https://www.gnu.org/software/inetutils/manual/html_node/rsh-invocation.html>.

- Execute a command on a remote host:

`rsh {{remote_host}} {{ls -l}}`

- Execute a command on a remote host with a specific username:

`rsh {{remote_host}} -l {{username}} {{ls -l}}`

- Redirect `stdin` to `/dev/null` when executing a command on a remote host:

`rsh {{remote_host}} --no-err {{ls -l}}`
