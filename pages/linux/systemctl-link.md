# systemctl link

> Link a unit file located outside the unit file search path into the search path.
> See also: `systemctl unlink`
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#link%20PATH%E2%80%A6>.

- Link a unit file to make it available for systemd commands:

`systemctl link /{{path/to/service}}`

- Link multiple unit files at once:

`systemctl link /{{path/to/service1 /path/to/service2 ...}}`
