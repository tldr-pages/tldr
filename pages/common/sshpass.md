# sshpass

> SSH password provider.

- SSH into a remote server using a password supplied on a file descriptor (fd):

`sshpass -d {{fd}} ssh {{user}}@{{hostname}}`

- SSH into a remote server with the password supplied as an option, and automatically accept unknown SSH keys:

`sshpass -p {{password}} ssh -o StrictHostKeyChecking=no {{user}}@{{hostname}}"`

- SSH into a remote server using the first line of a file as the password, automatically accept unknown SSH keys, and launch a command:

`sshpass -f {{file}} ssh -o StrictHostKeyChecking=no {{user}}@{{hostname}} "{{command}}"`
