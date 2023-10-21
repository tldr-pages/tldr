# slurmrestd

> Interface to Slurm via REST API. It can be used in two modes: *Inetd Mode* & *Listen Mode*
> More information: <https://slurm.schedmd.com/slurmrestd.html>.

- print a brief summary of command options:

`slurmrestd -h`

- Change group id (and drop supplemental groups) before processing client request:

`slurmrestd --g <group id>`

- Hostname and port to listen against:

`slurmrestd [host]:port`

- Listen on local UNIX socket:

`slurmrestd unix:/path/to/socket`

- Comma-delimited list of authentication plugins to load:

`slurmrestd -a <authentication plugins>`