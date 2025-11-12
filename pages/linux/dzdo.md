# dzdo

> A command-line utility similar to `sudo`, used to run commands with elevated privileges.
> Often used in enterprise environments with centralized access control (e.g., Active Directory).
> More information: <https://linux.die.net/man/8/dzdo>.

- Run a command as root:

`dzdo {{command}}`

- Edit a protected file:

`dzdo nano {{/etc/hosts}}`

- Update system packages:

`dzdo apt update`

- Switch to root shell:

`dzdo su -`
