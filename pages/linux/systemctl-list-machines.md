# systemctl list-machines

> List the host and all running local virtual machines or containers with their state.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#list-machines%20PATTERN%E2%80%A6>.

- Show all machines (host and running containers/VMs):

`systemctl list-machines`

- List a specific machine:

`systemctl list-machines {{machine}}`

- List multiple matching machines:

`systemctl list-machines {{machine_1 machine_2 ...}}`

- Filter machines using wildcard patterns ie, `shell-globbing`:

`systemctl list-machines {{pattern}}`
