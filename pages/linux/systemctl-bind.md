# systemctl bind

> Ephemerally bind-mount a file or directory from the host into a unit's mount namespace.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#bind%20UNIT%20PATH%20%5BPATH%5D>.

- Bind-mount a host path into the same location inside the unit:

`systemctl bind {{unit}} /{{path/to/host_directory}}`

- Bind-mount a host path into a different location inside the unit:

`systemctl bind {{unit}} /{{path/to/host_directory}} /{{path/to/unit_directory}}`

- Bind-mount a path as read-only inside the unit:

`systemctl bind {{unit}} /{{path/to/host_directory}} --read-only`

- Create the destination path inside the unit before binding:

`systemctl bind {{unit}} /{{path/to/host_directory}} /{{path/to/unit_directory}} --mkdir`
