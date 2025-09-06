# sshpass

> An SSH password provider.
> It works by creating a TTY, feeding the password into it, and then redirecting `stdin` to the SSH session.
> More information: <https://manned.org/sshpass>.

- Connect to a remote server using a password supplied on a file descriptor (in this case, `stdin`):

`sshpass -d {{0}} ssh {{user}}@{{hostname}}`

- Connect to a remote server with the password supplied as an option, and automatically accept unknown SSH keys:

`sshpass -p {{password}} ssh -o StrictHostKeyChecking=no {{user}}@{{hostname}}`

- Connect to a remote server using the first line of a file as the password, automatically accept unknown SSH keys, and launch a command:

`sshpass -f {{path/to/file}} ssh -o StrictHostKeyChecking=no {{user}}@{{hostname}} "{{command}}"`
