# distrobox-enter

> Enter a distrobox container. See also: `tldr distrobox`.
> Default command executed is your SHELL, but you can specify different shells or entire commands to execute. If used inside a script, an application, or a service, you can specify the --headless mode to disable tty and interactivity.
> More information: <https://distrobox.privatedns.org/usage/distrobox-enter.html>.

- Enter a distrobox container:

`distrobox-enter {{container-name}}`

- Enter a distrobox container and run `sh -l`:

`distrobox-enter container-name -- sh -l`

- Enter a distrobox without instantiating a tty:

`distrobox-enter -H container-name -- uptime -p`
