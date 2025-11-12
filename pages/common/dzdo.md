# dzdo

> Escalate privileges based on Active Directory.
> Similar to `sudo` but integrated with Active Directory for privilege management.
> More information: <https://manned.org/dzdo>.

- Run a command as the superuser:

`dzdo {{command}}`

- Run a command as another user:

`dzdo {{[-u|--user]}} {{user}} {{command}}`

- Edit a file as the superuser with your default editor:

`dzdo {{[-e|--edit]}} {{path/to/file}}`

- Launch the default shell with superuser privileges:

`dzdo {{[-s|--shell]}}`

- List the allowed commands for the invoking user:

`dzdo {{[-l|--list]}}`

- Display help:

`dzdo {{[-h|--help]}}`
