# systemd-nspawn

> Spawn a command or OS in a light-weight container.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemd-nspawn.html>.

- Run a command in a container:

`systemd-nspawn -D {{path/to/container/root}}`

- Run a full Linux-based OS in a container:

`systemd-nspawn --boot -D {{path/to/container/root}}`

- Run the specified command as PID 2 in the container (as opposed to PID 1). Use a stub init process:

`systemd-nspawn -D {{path/to/container/root}} --as-pid2`

- Specify the machine name and hostname:

`systemd-nspawn --machine={{mycontainer}} --hostname={{mycontainerhost}} -D {{path/to/container/root}}`