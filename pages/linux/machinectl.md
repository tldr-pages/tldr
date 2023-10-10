# machinectl

> Utility to manage Linux containers, particularly on systems that use the `systemd init` system.
> It provides a powerful and convenient way to create, start, stop, and manage container instances, referred to as machines in `systemd` terminology.
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
