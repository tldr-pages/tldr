# distrobox-enter

> Enter a distrobox container. More about distrobox: `tldr distrobox`.
> Default command executed is your SHELL, but you can specify different shells or entire commands to execute. If used inside a script, an application, or a service, you can specify the --headless mode to disable tty and interactivity.
> More information: <https://github.com/89luca89/distrobox/blob/main/docs/usage/distrobox-enter.md>.

- Enter a distrobox:

`distrobox-enter {{container-name}}`

- Enter a distrobox and run `sh -l`:

`distrobox-enter container-name -- sh -l`

- Enter a distrobox without instantiating a tty:

`distrobox-enter -H container-name -- uptime -p`
