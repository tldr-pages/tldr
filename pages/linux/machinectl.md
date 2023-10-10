# machinectl

> Control the systemd machine manager.
> Execute operations on virtual machines, containers and images.
> More information: <https://www.freedesktop.org/software/systemd/man/machinectl.html>.

- Create a container:

`sudo machinectl create {{container-name}}`

- Start a container:

`sudo machinectl start {{container-name}}`

- Stop a running container:

`sudo machinectl stop {{container-name}}`

- Display a list of running containers:

`machinectl list`

- Interactively log into the container shell:

`sudo machinectl shell {{container-name}}`
