# distrobox-enter

> Enter a Distrobox container. See also: `tldr distrobox`.
> Default command executed is your SHELL, but you can specify different shells or entire commands to execute. If used inside a script, an application, or a service, you can use the `--headless` mode to disable the tty and interactivity.
> More information: <https://distrobox.it/usage/distrobox-enter>.

- Enter a Distrobox container:

`distrobox-enter {{container_name}}`

- Enter a Distrobox container and run a command at login:

`distrobox-enter {{container_name}} -- {{sh -l}}`

- Enter a Distrobox container without instantiating a tty:

`distrobox-enter --name {{container_name}} -- {{uptime -p}}`
