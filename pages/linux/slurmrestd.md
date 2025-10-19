# slurmrestd

> Interface to Slurm via REST API. It can be used in two modes: *Inetd Mode* & *Listen Mode*.
> More information: <https://slurm.schedmd.com/slurmrestd.html>.

- Change the [g]roup ID (and drop supplemental groups) before processing client requests:

`slurmrestd -g {{group_id}} {{[host]:port|unix:/path/to/socket}}`

- Comma-delimited list of [a]uthentication plugins to load:

`slurmrestd -a {{authentication_plugins}} {{[host]:port|unix:/path/to/socket}}`

- Read Slurm configuration from the specified [f]ile:

`slurmrestd -f {{path/to/file}}`

- Change [u]ser ID before processing client request:

`slurmrestd -u {{user_id}}`

- Display [h]elp:

`slurmrestd -h`

- Display [V]ersion:

`slurmrestd -V`
