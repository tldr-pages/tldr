# sshpass

> An ssh password provider.
> It works by creating a TTY, feeding the password into it, and then redirecting stdin to the ssh session.

- ssh into a remote server using a password supplied on a file descriptor (fd):

`sshpass -d {{fd}} ssh {{user}}@{{hostname}}`

- ssh into a remote server with the password supplied as an option, and automatically accept unknown ssh keys:

`sshpass -p {{password}} ssh -o StrictHostKeyChecking=no {{user}}@{{hostname}}"`

- ssh into a remote server using the first line of a file as the password, automatically accept unknown ssh keys, and launch a command:

`sshpass -f {{file}} ssh -o StrictHostKeyChecking=no {{user}}@{{hostname}} "{{command}}"`
