# systemctl kexec

> Reboot the system via kexec.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#kexec>.

- Fast reboot using kexec (if kernel is pre-loaded)

`systemctl kexec`

- Force normal reboot even if kexec is available

`systemctl kexec --force`
