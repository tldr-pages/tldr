# systemd-analyze

> Show timing details about the boot process of units (services, mount points, devices, sockets).

- List time of each unit to start up:

`systemd-analyze blame`

- Print a tree of the time critical chain of units:

`systemd-analyze critical-chain`

- Create an SVG file showing when each system service started, highlighting the time that they spent on initialization:

`systemd-analyze plot > {{path/to/file.svg}}`

- Plot a dependency graph and convert it to an SVG file:

`systemd-analyze dot | dot -T{{svg}} > {{path/to/file.svg}}`
