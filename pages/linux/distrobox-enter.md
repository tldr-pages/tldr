# distrobox enter

> Enter a Distrobox container. The default command is the user's `$SHELL`.
> Put the command to run after `--`. Use `--no-tty` when there is no interactive terminal.
> See also: `distrobox`.
> More information: <https://distrobox.it/usage/distrobox-enter/>.

- Enter a container:

`distrobox enter {{container_name}}`

- Enter a container and run `sh` as a login shell:

`distrobox enter {{container_name}} -- sh -l`

- Enter a container and run a command without instantiating a tty:

`distrobox enter {{[-n|--name]}} {{container_name}} {{[-T|--no-tty]}} -- {{command}}`

- Display help:

`distrobox enter {{[-h|--help]}}`
