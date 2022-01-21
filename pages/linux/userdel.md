# userdel

> Remove a user account or remove a user from a group.
> See also: `users`, `useradd`, `usermod`.
> More information: <https://manned.org/userdel>.

- Remove a user:

`sudo userdel {{username}}`

- Remove a user in other root directory:

`sudo userdel --root {{path/to/other/root}} {{username}}`

- Remove a user along with the home directory and mail spool:

`sudo userdel --remove {{username}}`
