# systemd-analyze

> Show timing details about the boot process of units (services, mount points, devices, sockets).

- List time of each unit to start up:

`systemd-analyze blame`

- Print a tree of the time critical chain of units:

`systemd-analyze critical-chain`
