# systemd-repart

> Automatically grow and add partitions.
> Grows and adds partitions based on the configuration files described in repart.d.
> Does not automatically resize file system on partition. See systemd-growfs to extend file system.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-repart.html>.

- Grow the root partition (/) to all available disk space:

`systemd-repart`

- View changes without applying:

`systemd-repart --dry-run=yes`

- Grow root partition size to 10 gigabytes:

`systemd-repart --size=10G --root /`
