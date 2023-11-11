# rexec

> Execute a command on a remote host.
> Note: Use `rexec` with caution, as it transmits data in plain text. Consider secure alternatives like `ssh` for encrypted communication.
> More information: <https://www.gnu.org/software/inetutils/manual/html_node/rexec-invocation.html>.

- Execute a command on a remote [h]ost:

`rexec -h={{remote_host}} {{ls -l}}`

- Specify the remote [u]sername on a remote [h]ost:

`rexec -username={{username}} -h={{remote_host}} {{ps aux}}`

- Redirect `stdin` from `/dev/null` on a remote [h]ost:

`rexec --no-err -h={{remote_host}} {{ls -l}}`

- Specify the remote [P]ort on a remote [h]ost:

`rexec -P={{1234}} -h={{remote_host}} {{ls -l}}`
