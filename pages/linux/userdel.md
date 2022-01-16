# userdel

> Remove a user account or remove a user from a group.
> Note: all commands must be executed as root.
> More information: <https://manned.org/userdel>.

- Remove a user:

`userdel {{user_name}}`

- Remove a user from the group:

`userdel {{user_name}} {{group_name}}`

- Remove a user in other root directory:

`userdel --root {{path/to/other/root}} {{user_name}}`

- Remove a user along with the home directory and mail spool:

`userdel --remove {{user_name}}`
