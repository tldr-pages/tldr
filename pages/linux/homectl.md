# homectl

> Create, remove, change or inspect home directories using the systemd-homed service.
> More information: <https://man.archlinux.org/man/homectl.1>.

- List home areas:

`homectl list`

- Create a home area (the user and the associated home directory):

`sudo homectl create {{username}}`

- Remove a specific user and the associated home directory:

`sudo homectl remove {{username}}`

- Change the password for a specific user:

`sudo homectl passwd {{username}}`

- Run shell or a command with access to a specific home area:

`sudo homectl with {{username}} -- {{command}} {{command_arguments}}`

- Lock/unlock a user home area:

`sudo homectl {{lock|unlock}} {{username}}`

- Resize a home area to 100 GiB:

`sudo homectl resize {{username}} {{100G}}`

- Display help:

`homectl --help`
