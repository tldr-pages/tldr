# slurmrestd

> Interface to Slurm via REST API. It can be used in two modes: *Inetd Mode* & *Listen Mode*.
> More information: <https://slurm.schedmd.com/slurmrestd.html>.

- Print a brief summary of command options:

`slurmrestd -h`

- Change group id (and drop supplemental groups) before processing client request:

`slurmrestd --g {{group id}} {{[host]:port | unix:/path/to/socket}}`

- Comma-delimited list of authentication plugins to load:

`slurmrestd -a {{authentication plugins}} {{[host]:port | unix:/path/to/socket}}`

- Read Slurm configuration from the specified file:

`slurmrestd -f`

- Change user id before processing client request:

`slurmrestd -u {{user id}}`

- Print version information and exit:

`slurmrestd -V`
