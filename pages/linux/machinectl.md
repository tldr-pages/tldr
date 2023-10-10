# machinectl

> Control the systemd machine manager.
> Execute operations on virtual machines, containers and images.
> More information: <https://www.freedesktop.org/software/systemd/man/machinectl.html>.

- Create a container:

`sudo machinectl create {{container-name}}`

- Start a machine as a service using `systemd-nspawn`:

`sudo machinectl start {{machine_name}}`

- Stop a running machine:

`sudo machinectl stop {{machine_name}}`

- Display a list of running containers:

`machinectl list`

- Interactively log into the container shell:

`sudo machinectl shell {{container-name}}`
