# systemctl bind

> Ephemerally bind-mount a file or directory from the host into a unit's mount namespace.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#%0A%20%20%20%20%20%20%20%20%20%20%20%20bind%0A%20%20%20%20%20%20%20%20%20%20%20%20UNIT%0A%20%20%20%20%20%20%20%20%20%20%20%20PATH%0A%20%20%20%20%20%20%20%20%20%20%20%20%5BPATH%5D%0A%20%20%20%20%20%20%20%20%20%20>.

- Bind-mount a host path into the same location inside the unit:

`systemctl bind {{unit}} {{/path/on/host}}`

- Bind-mount a host path into a different location inside the unit:

`systemctl bind {{unit}} {{/path/on/host}} {{/path/in/unit}}`

- Bind-mount a path as read-only inside the unit:

`systemctl bind --read-only {{unit}} {{/path/on/host}}`

- Create the destination path inside the unit before binding:

`systemctl bind --mkdir {{unit}} {{/path/on/host}} {{/path/in/unit}}`
