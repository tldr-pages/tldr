# runuser

> Run commands as a user and group without asking for password (needs root privileges).
> More information: <https://manned.org/runuser>.

- Run command as a different user:

`runuser {{user}} -c '{{command}}'`

- Run command as a different user and group:

`runuser {{user}} -g {{group}} -c '{{command}}'`

- Start a login shell as a specific user:

`runuser {{user}} -l`

- Specify a shell for running instead of the default shell (also works for login):

`runuser {{user}} -s {{/bin/sh}}`

- Preserve the entire environment of root (only if `--login` is not specified):

`runuser {{user}} --preserve-environment -c '{{command}}'`
