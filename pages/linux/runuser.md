# runuser

> Run commands as a specific user and group IDs.
> Does not ask for password. Only useful when run as the root user.

- Run 'command' under substitute 'user':

`runuser {{user}} -c '{{command}}'`

- Run 'command' under substitute 'user' and 'group':

`runuser {{user}} -g {{group}} -c '{{command}}'`

- Start a login shell as a specific user:

`runuser {{user}} -l`

- Specific a 'shell' for running or login instead of default shell:

`runuser {{user}} -l -s /bin/sh`

- Preserve the entire environment of root (if running by root). Ignore when having option `--login`:

`runuser {{user}} --preserve-environment -c '{{command}}'`
