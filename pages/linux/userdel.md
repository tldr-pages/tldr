# userdel

> Remove a user account or remove a user from a group.
> Note: all commands must be executed as root.
> More information: <https://manned.org/userdel>.

- Remove a user:

`userdel {{name}}`

- Remove a user along with their home directory and mail spool:

`userdel --remove {{name}}`

- Remove a user from a group:

`userdel {{name}} {{group}}`

- Remove a user in other root directory:

`userdel --root {{path/to/other/root}} {{name}}`
