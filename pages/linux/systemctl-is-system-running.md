# systemctl is-system-running

> Check the current state of the system.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#is-system-running>.

- Check whether the system is operational and print the current state:

`systemctl is-system-running`

- Check and print the current state quietly (no output, only exit status):

`systemctl is-system-running {{[-q|--quiet]}}`

- Wait until the boot process is completed before printing the current state:

`systemctl is-system-running --wait`
