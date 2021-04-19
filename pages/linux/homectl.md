# homectl

> Create, remove, change or inspect home directories using the systemd-homed service.
> More information: <https://manned.org/homectl>.

- List user accounts and their associated home directories:

`homectl list`

- Create a user account and their associated home directory:

`sudo homectl create {{username}}`

- Remove a specific user and the associated home directory:

`sudo homectl remove {{username}}`

- Change the password for a specific user:

`sudo homectl passwd {{username}}`

- Run a shell or a command with access to a specific home directory:

`sudo homectl with {{username}} -- {{command}} {{command_arguments}}`

- Lock or unlock a specific home directory:

`sudo homectl {{lock|unlock}} {{username}}`

- Change the disk space assigned to a specific home directory to 100 GiB:

`sudo homectl resize {{username}} {{100G}}`

- Display help:

`homectl --help`
