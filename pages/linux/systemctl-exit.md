# systemctl exit

> Ask the service manager to quit.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#exit%20EXIT_CODE>.

- Exit the user service manager:

`systemctl exit --user`

- Exit the user service manager with a specific exit code:

`systemctl exit {{code}} --user`

- Ask the container's service manager to exit (equivalent of `systemctl poweroff` if not in a container):

`systemctl exit`
