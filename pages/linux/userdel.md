# userdel

> Remove a user account or remove a user from a group.
> Note: all commands must be executed as root.
> More information: <https://manned.org/userdel>.

- Remove a user:

`userdel {{user}}`

- Remove a user in other root directory:

`userdel --root {{path/to/other/root}} {{user}}`

- Remove a user along with the home directory and mail spool:

`userdel --remove {{user}}`
