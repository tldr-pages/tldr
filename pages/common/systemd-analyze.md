# systemd-analyze

> Analyze and debug systemd boot performance and unit dependencies.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-analyze.html>.

- Show the total boot time and a breakdown by kernel, initrd, and userspace:

`systemd-analyze time`

- List all running units sorted by initialization time:

`systemd-analyze blame`

- Print a tree of time-critical chain of units:

`systemd-analyze critical-chain`

- Generate an SVG plot of the boot process and save it to a file:

`systemd-analyze plot > {{path/to/file.svg}}`

- Show security-related information about a running service:

`systemd-analyze security {{service_name}}`

- Verify the syntax and dependencies of all unit files:

`systemd-analyze verify {{/path/to/unit.file}}`
