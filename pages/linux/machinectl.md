# machinectl

> Control the systemd machine manager.
> Execute operations on virtual machines, containers and images.
> More information: <https://www.freedesktop.org/software/systemd/man/machinectl.html>.

- Start a machine as a service using `systemd-nspawn`:

`sudo machinectl start {{machine_name}}`

- Stop a running machine:

`sudo machinectl stop {{machine_name}}`

- Display a list of running machines:

`machinectl list`

- Open an interactive shell inside the machine:

`sudo machinectl shell {{machine_name}}`
