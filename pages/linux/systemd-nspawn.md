# systemd-nspawn

> Spawn a command or OS in a lightweight container.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemd-nspawn.html>.

- Run a command in a container:

`systemd-nspawn --directory {{path/to/container_root}}`

- Run a full Linux-based OS in a container:

`systemd-nspawn --boot --directory {{path/to/container_root}}`

- Run the specified command as PID 2 in the container (as opposed to PID 1) using a stub init process:

`systemd-nspawn --directory {{path/to/container_root}} --as-pid2`

- Specify the machine name and hostname:

`systemd-nspawn --machine={{container_name}} --hostname={{container_host}} --directory {{path/to/container_root}}`
