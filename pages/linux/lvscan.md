# lvscan

> Scan (list) all logical volumes in the system.
> Part of the LVM (Logical Volume Manager) suite.
> More information: <https://manned.org/lvscan>.

- List all logical volumes:

`sudo lvscan`

- List only active logical volumes:

`sudo lvscan --active`

- List only inactive logical volumes:

`sudo lvscan --inactive`

- Display logical volumes in JSON format:

`sudo lvscan --reportformat json`
