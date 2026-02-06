# runuser

> Run commands as a user and group without asking for password.
> More information: <https://manned.org/runuser>.

- Run command as a different user:

`sudo runuser {{user}} {{[-c|--command]}} '{{command}}'`

- Run command as a different user and group:

`sudo runuser {{user}} {{[-g|--group]}} {{group}} {{[-c|--command]}} '{{command}}'`

- Start a login shell as a specific user:

`sudo runuser {{user}} {{[-l|--login]}}`

- Specify a shell for running instead of the default shell (also works for login):

`sudo runuser {{user}} {{[-s|--shell]}} {{/bin/sh}}`

- Preserve the entire environment of root (only if `--login` is not specified):

`sudo runuser {{user}} {{[-p|--preserve-environment]}} {{[-c|--command]}} '{{command}}'`
