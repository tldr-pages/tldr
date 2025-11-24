# systemctl link

> Link a unit file located that is not in the unit file search path.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#link%20PATH%E2%80%A6>.

- Link a unit file to make it available for systemd commands:

`systemctl link {{absolute_path/to/service}}`

- Link multiple unit files at once:

`systemctl link {{absolute_path/to/service_1 absolute_path/to/service_2 ...}}`
