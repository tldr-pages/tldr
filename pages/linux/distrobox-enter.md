# distrobox-enter

> Run a command in a Distrobox container.
> Default command executed is your SHELL, but you can specify different shells or entire commands to execute. If used inside a script, an application, or a service, you can specify the --headless mode to disable tty and interactivity.
> More information: <https://distrobox.privatedns.org>.

- Enter a distrobox and run `sh -l`:

`distrobox-enter container-name -- sh -l`

- Enter a distrobox without instantiating a tty:

`distrobox-enter -H container-name -- uptime -p`
