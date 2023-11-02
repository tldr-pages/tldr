# systemd-nspawn

> Spawn a command or OS in a light-weight container.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemd-nspawn.html>.

- Run a command in a container:

`systemd-nspawn -D {{path/to/container/root}}`

- Run a full Linux-based OS in a container:

`systemd-nspawn --boot -D {{path/to/container/root}}`

- By default, the command you specify is run as PID 1 (init) in the container. To run it as PID 2 with a stub init process:

`systemd-nspawn -D {{/path/to/container/root}} --as-pid2`

- Specify the machine name and hostname:

`systemd-nspawn --machine="{{mycontainer}}" --hostname="{{mycontainerhost}}" -D {{/path/to/container/root}}`