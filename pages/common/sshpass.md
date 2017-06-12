# sshpass

> Non-interactive SSH password provider.

- SSH into a remote server using a password supplied on a file descriptor (fd):

`sshpass -d {{fd}} ssh -o StrictHostKeyChecking=no {{user}}@{{hostname}} -- "{{command}}"`

- SSH into a remote server with the password supplied as an option:

`sshpass -p {{password}} ssh -o StrictHostKeyChecking=no {{user}}@{{hostname}} -- "{{command}}"`

- SSH into a remote server using the first line of a file as the password:

`sshpass -f {{file}} ssh -o StrictHostKeyChecking=no {{user}}@{{hostname}} -- "{{command}}"`
