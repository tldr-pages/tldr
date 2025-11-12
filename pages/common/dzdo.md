# dzdo

> Execute privileged commands as root or another user via Active Directory roles.
> Similar to `sudo` but integrated with Delinea; supports Ansible become plugin.
> More information: <https://docs.delinea.com/online-help/server-suite/commandref/centrify-command-reference-2025.pdf>.

- Run a command with elevated privileges:

`dzdo {{command}}`

- Run a command as another user:

`dzdo -u {{user}} {{command}}`

- Edit a file with elevated privileges using the default editor:

`dzdo -e {{path/to/file}}`

- Launch an interactive login shell with elevated privileges:

`dzdo -i`

- Launch the default shell with elevated privileges:

`dzdo -s`

- List allowed commands for the current user:

`dzdo -l`

- Validate and update authentication timestamp:

`dzdo -v`

- Display version information:

`dzdo -V`
