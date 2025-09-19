# systemctl exit

> Ask the service manager to quit.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#exit%20EXIT_CODE>.

- Exit the user service manager:

`systemctl --user exit`

- Exit the user service manager with a specific exit code:

`systemctl --user exit {{code}}`

- Ask the container’s service manager to exit (equivalent of `systemctl poweroff` if not in a container):

`systemctl exit`
