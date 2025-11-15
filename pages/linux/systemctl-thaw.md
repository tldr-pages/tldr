# systemctl thaw

> Thaw (resume) one or more frozen units.
> Units can be frozen with `systemctl freeze`.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#thaw%20PATTERN%E2%80%A6>.

- Thaw a specific unit:

`systemctl thaw {{unit}}`

- Thaw multiple units:

`systemctl thaw {{unit1 unit2 ...}}`

- Thaw all currently frozen units:

`systemctl thaw '*'`
