# flatpak enter

> Enter the namespace of a running Flatpak application.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-enter>.

- Run an interactive shell inside a running Flatpak instance (use `flatpak ps` to find the instance ID):

`flatpak enter {{instance_id}} {{sh}}`

- Run a specific command inside a running Flatpak instance:

`flatpak enter {{instance_id}} {{command}}`

- Run a command with arguments inside a running Flatpak instance:

`flatpak enter {{instance_id}} {{command}} {{arg1 arg2 ...}}`
